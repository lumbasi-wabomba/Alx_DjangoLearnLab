from django.urls import path
from .views import LoginView, LogoutView, RegisterView, ProfileManagementView
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView, CommentDetailView

urlpatterns = [
    path('login/', LoginView.as_view({'get': 'login'}), name='login'),
    path('logout/', LogoutView.as_view({'post': 'logout'}), name='logout'),
    path('register/', RegisterView.as_view({'post': 'register'}), name='register'),
    path('profile/', ProfileManagementView.as_view({'get': 'view_profile'}), name='profile'),
    path('profile/update/', ProfileManagementView.as_view({'post': 'update_profile'}), name='update_profile'),
    path('profile/view/', ProfileManagementView.as_view({'get': 'view_profile'}), name='view_profile'),
    path('profile/delete/', ProfileManagementView.as_view({'post': 'delete_profile'}), name='delete_profile'),
    path('post/', ListView.as_view({'get': 'list_posts'}), name='post_list'),
    path('post/<int:post_id>/', DetailView.as_view({'get': 'post_detail'}), name='post_detail'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/update/', UpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/delete/', DeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view({'post': 'add_comment'}), name='add_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/edit/', CommentUpdateView.as_view({'post': 'edit_comment'}), name='edit_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/', CommentDetailView.as_view({'get': 'view_comment'}), name='view_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', CommentDeleteView.as_view({'post': 'delete_comment'}), name='delete_comment'),
]
