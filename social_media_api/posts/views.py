from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
# Create your views here.

class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        post = serializer.save(author = self.request.user)

        return Response(
            UserSerializer(post).data,
            status=HTTP_200_OK
        )
    
class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        comment = serializer.save(user = self.request.user)

        return Response(
            UserSerializer(comment).data,
            status=HTTP_200_OK
        )
    
class CommentsView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UpdatePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You must be the author to modify this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You must be the author to delete this post.")
        instance.delete()


class UpdateCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.user != self.request.user: 
            raise PermissionDenied("You must be the author to modify this comment.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user: 
            raise PermissionDenied("You must be the author to delete this comment.")
        instance.delete()
