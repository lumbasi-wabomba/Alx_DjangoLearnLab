from django.urls import path
from .views import PostCreateView, CommentCreateView, CommentsView, UpdateCommentView, UpdatePostView, UpdateCommentView

urlpatterns = [
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", UpdatePostView.as_view(), name="post-detail"),
    path("comments/", CommentsView.as_view(), name="comment-list"),
    path("comments/create/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", UpdateCommentView.as_view(), name="comment-detail"),
]
