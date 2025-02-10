from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    context_object_name = "post"


class CommentList(generic.ListView):
    queryset = Comment.objects.all()
    template_name = "comment_list.html"
    context_object_name = "comment"