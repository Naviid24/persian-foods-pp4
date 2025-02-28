from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Post, Like, Comment
from .forms import CommentForm, PostForm
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    ListView,
    DeleteView
)
from django.db.models import Q
from django.contrib.auth.mixins import( 
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy


class IndexView(TemplateView):
    """
    View to display home page.
    """
    template_name = "blog/index.html"


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'blog/404.html', status=404)


class PostList(generic.ListView):
    """View to list published blog posts with pagination."""
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/posts_list.html"
    paginate_by = 4  # Controls pagination


def post_detail(request, slug):
    """
    Display an individual blog post with comments.

    Context:
        post (Post): The blog post.
        comments (QuerySet): All comments for the post.
        comment_count (int): Number of approved comments.
        comment_form (CommentForm): Form for submitting new comments.

    Template:
        blog/post_detail.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()

    user_likes = Like.objects.filter(post=post, user=request.user).exists() if request.user.is_authenticated else False

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')

    # Reset comment form for next submission
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "user_likes": user_likes
        },
    )


def like_post(request, post_id):
    """
    Handles liking and unliking of a post via AJAX.

    Returns:
        JsonResponse: Contains `liked` status and total likes count.
    """
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()  # Unlike the post
        liked = False
    else:
        liked = True

    return JsonResponse({"liked": liked, "total_likes": post.likes.count()})


def comment_edit(request, slug, comment_id):
    """
    Handles editing of a user's comment.

    Redirects to:
        post_detail page after editing.
    """
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug, status=1)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.user != request.user:
            messages.error(request, "You can only edit your own comments.")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Require re-approval after editing
            comment.save()
            messages.success(request, 'Comment updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Handles deletion of a user's comment.

    Redirects to:
        post_detail page after deletion.
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, CreateView):
    """
    Class based view to add/create recipes
    Requires user to be logged in.
    On successful form submission, redirects to the 'recipes' page.
    If the form is valid, sets the author of the recipe
    to the current logged-in user.
    Displays a success message to the user.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    success_url = reverse_lazy('posts_list')

    # Source: https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post # noqa
    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your post has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super(AddPost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Class based view to edit/update recipe
    Requires the user to be logged in and be the author of the recipe.
    On successful form submission, redirects to the 'recipes' page.
    Handles the form submission when valid.
    Displays a success message to the user
    on successful update.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/update_post.html"
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your post has been updated successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class base view to delete a post.
    To make sure user is the author of the post,
    and make sure user is authenticated to view,
    the delete button
    """

    model = Post
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        return self.request.user == self.get_object().author

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        messages.success(
            request, f'Your post "{post.title}"has been deleted successfully!')
        return super().delete(request, *args, **kwargs)
    

class UserDrafts(ListView):
    """
    Class based view to display user's draft recipes.
    Displays drafts created by the currently logged-in user.
    Only visible to the draft author.
    Returns a list of recipes with status of 'draft'.
    Displays 6 recipes per page.
    """

    template_name = "blog/my_drafts.html"
    model = Post
    context_object_name = "post_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user, status=0)


class PostSearchList(ListView):
    """
    View to display a list of posts based on user search.
    Searches for recipes based on title.
    Retrieves search for only recipes with status 'published'.
    Displays 6 recipes per page.
    """
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query),
                status=1
            ).order_by('-created_on')
        else:
            queryset = Post.objects.none()
        return queryset


