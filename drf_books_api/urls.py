"""
URL configuration for drf_books_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books.views.sample import sample_list_view, sample_create_view, sample_update_view, sample_delete_view
from books.views.books import create_book, list_books, update_book, delete_book
from books.views.auth import register, login, logout

urlpatterns = [
    path('api/sample/list/', sample_list_view, name='sample-list'),
    path('api/sample/create/', sample_create_view, name='sample-create'),
    path('api/sample/update/', sample_update_view, name='sample-update'),
    path('api/sample/delete/', sample_delete_view, name='sample-delete'),
    path('api/books/', list_books, name='list-books'),
    path('api/books/create/', create_book, name='create-book'),
    path('api/books/<str:book_id>/update/', update_book, name='update-book'),
    path('api/books/<str:book_id>/delete/', delete_book, name='delete-book'),
    path('api/auth/register/', register, name='register'),
    path('api/auth/login/', login, name='login'),
    path('api/auth/logout/', logout, name='logout'),
]
