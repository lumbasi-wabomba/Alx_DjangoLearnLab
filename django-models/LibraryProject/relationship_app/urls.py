from django.urls import path
from . import views
from .views import LibraryDetailview, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('profile/', views.profile, name='profile'),
]
