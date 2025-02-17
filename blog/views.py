from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Like, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required




class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    #control pagination
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(post=post, user=request.user).exists()
    else:
        user_likes = False


    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    # Make comment area ready for next comment
    comment_form = CommentForm()

    print("About to render template")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
        },
    )


# 404
def custom_404(request, exception):
    return render(
        request,
        'blog/404.html',
        status=404
    )



@login_required
def like_post(request, post_id):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "You must be logged in to like a post."}, status=403)

    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    

    if not created:
        like.delete()  # If like exists, unlike the post
        liked = False
    else:
        liked = True

    return JsonResponse({"liked": liked, "total_likes": post.likes.count()})



def comment_edit(request, slug, comment_id):
    """
     To edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))