from django.urls import path
from relationship_app import views
from relationship_app.views import (
    LibraryDetailview,
    LoginView,
    LogoutView,
)
from .views import list_books, LibraryDetailView
from .views import add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  
    path('profile/', views.profile, name='profile'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/add_book/', add_book_view, name='add_book'),
    path('books/<int:pk>/edit_book/', edit_book_view, name='edit_book'),
    path('books/<int:pk>/delete_book/', delete_book_view, name='delete_book'),
]
