from django.urls import path
from .views import Login, Logout, Register, ProfileManagement

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
    path('profile/', ProfileManagement, name='profile'),
]
