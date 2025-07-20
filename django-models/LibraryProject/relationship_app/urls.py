from django.contrib import admin
from django.urls import path
from relationship_app import views
from relationship_app.views import LibraryDetailview  
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),  
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile')
]
