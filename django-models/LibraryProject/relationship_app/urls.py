from django.urls import path
from . import views  # Use relative import for views inside the same app

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', views.LibraryDetailview.as_view(), name='library'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
]
