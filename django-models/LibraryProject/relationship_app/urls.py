from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', views.library_detail, name='library'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
