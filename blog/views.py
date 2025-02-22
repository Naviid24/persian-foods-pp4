from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """View to list published blog posts with pagination."""
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
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
            "user_likes": user_likes,
        },
    )


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'blog/404.html', status=404)


def custom_500(request):
    return render(request, 'blog/500.html', status=500)


@login_required
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


@login_required
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


@login_required
def comment_delete(request, slug, comment_id):
    """
    Handles deletion of a user's comment.

    Redirects to:
        post_detail page after deletion.
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))