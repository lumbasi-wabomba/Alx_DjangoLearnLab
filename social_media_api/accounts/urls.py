from django.urls import path
from .views import  RegisterView, LoginView, UserViewSet, LogoutView, ProfileView, Follow_userView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', Follow_userView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', Follow_userView.as_view(), name='unfollow_user'),
]

urlpatterns += router.urls
