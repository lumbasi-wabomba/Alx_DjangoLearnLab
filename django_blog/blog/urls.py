from django.urls import path
from .views import Login, Logout, Register, ProfileManagement
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
    path('profile/', ProfileManagement, name='profile'),
    path('profile/update/', ProfileManagement.as_view({'post': 'update_profile'}), name='update_profile'),
    path('profile/view/', ProfileManagement.as_view({'get': 'view_profile'}), name='view_profile'),
    path('profile/delete/', ProfileManagement.as_view({'post': 'delete_profile'}), name='delete_profile'),
    path('post/', ListView.as_view({'get': 'list_posts'}), name='post_list'),
    path('post/<int:pk>/', DetailView.as_view({'get': 'post_detail'}), name='post_detail'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post_delete'),
]
