from django.urls import path
from .views import PostView, CommentView

urlpatterns = [
    path('feed/', PostView.as_view(), name= 'feed'),
    path('comment/', CommentView.as_view(), name='comments')
]