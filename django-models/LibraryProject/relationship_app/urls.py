from django.urls import path
from .views import (
    function_based_view_book,
    LibraryDetailview,
    LoginView,
    LogoutView,
    RegisterView,
    profile,
)

urlpatterns = [
    path('books/', function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('profile/', profile, name='profile'),
]
