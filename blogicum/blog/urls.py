from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'category/<slug:slug>/',
        views.CategoryPostsView.as_view(),
        name='category_posts'
    ),
    path(
        'profile/<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
    path(
        'profile/<str:username>/edit/',
        views.ProfileEditView.as_view(),
        name='edit_profile'
    ),
    path(
        'posts/create/',
        views.PostCreateView.as_view(),
        name='create_post'
    ),
    path(
        'posts/<int:pk>/edit/',
        views.PostEditView.as_view(),
        name='edit_post'
    ),
    path(
        'posts/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),
    path(
        'posts/<int:pk>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        'posts/<int:pk>/edit_comment/<int:comment_id>/',
        views.CommentEditView.as_view(),
        name='edit_comment'
    ),
    path(
        'posts/<int:pk>/delete_comment/<int:comment_id>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment'
    ),
    path(
        'registration/',
        views.RegistrationView.as_view(),
        name='registration'
    ),
]
