from django.urls import path
from .views import PostView, CommentView

urlpatterns = [
    path('post/feed/', PostView.as_view(), name= 'feed'),
    path('post/comment/', CommentView.as_view(), name='comments')
]