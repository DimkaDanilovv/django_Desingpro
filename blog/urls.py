from django.urls import path
from .views import (
    category_delete,
    post_create,
    post_delete,
    post_detail,
    post_edit,
    post_list,
    category_create,
    category_detail,
    category_edit,
    category_list,
)

urlpatterns = [
    path('', post_list, name='blog-home'),

    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('posts/', post_list, name='post_list'),
    path('posts/<str:username>', post_list, name='post_list'),

    path('category/', category_list, name='category_list'),
    path('category/new/', category_create, name='category_create'),
    path('category/<int:pk>/', category_detail, name='category_detail'),

    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]