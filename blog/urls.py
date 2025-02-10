from . import views
from django.urls import path


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
]