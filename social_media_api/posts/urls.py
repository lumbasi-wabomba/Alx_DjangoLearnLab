from django.urls import path
from .views import LikeView, PostView, CommentView

urlpatterns = [
    path('post/feed/', PostView.as_view(), name= 'feed'),
    path('post/comment/', CommentView.as_view(), name='comments'),
    path('post/<int:pk>/like/', LikeView.as_view(), name='like'),
    path('post/<int:pk>/unlike/', LikeView.as_view(), name='unlike'),
]