from . import views
from django.urls import path
from .views import (
    IndexView,
    PostList,
    AddPost,
    UpdatePost,
    UserDrafts,
    PostSearchList,
    like_post,
    DeletePost
)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('posts_list/', PostList.as_view(), name='posts_list'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post_search/', PostSearchList.as_view(), name='post_search'),
    path('post_drafts/', UserDrafts.as_view(), name='post_drafts'),
    path('edit_post/<slug:slug>/', UpdatePost.as_view(),
         name='update_post'),
    path('<slug:slug>/delete', DeletePost.as_view(),
         name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'), 
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

