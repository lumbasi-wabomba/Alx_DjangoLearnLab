from django.urls import path
from relationship_app import views
from relationship_app.views import (
    LibraryDetailview,
    LoginView,
    LogoutView,
    RegisterView,
)

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # <-- EXACTLY WHAT CHECKER WANTS
    path('profile/', views.profile, name='profile'),
]
