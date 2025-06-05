from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Основные страницы
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),

    # Профиль пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Создание, редактирование и удаление постов
    path('posts/create/', views.PostCreateView.as_view(),
         name='create_post'),
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(),
         name='edit_post'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(),
         name='delete_post'),

    # Комментарии
    path('posts/<int:post_id>/comment/', views.add_comment,
         name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.CommentUpdateView.as_view(), name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.CommentDeleteView.as_view(), name='delete_comment'),
]
