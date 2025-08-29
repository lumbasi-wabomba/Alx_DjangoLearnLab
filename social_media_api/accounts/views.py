from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import CustomUser   
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token 
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'username'

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        return Response(
            UserSerializer(user).data,
            status=HTTP_200_OK
        )

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_data': UserSerializer(user).data
        }, status=HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_profile(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update_profile(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Follow_userView(APIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def follow_user(self, username, request):
        user = CustomUser.objects.filter(username=username).first()
        if not user:
            return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)
        request.user.following.add(user)
        return Response({"message": f"You are now following {username}"}, status=HTTP_200_OK)

    def unfollow_user(self, username, request):
        user = CustomUser.objects.filter(username=username).first()
        if not user:
            return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)
        request.user.following.remove(user)
        return Response({"message": f"You have unfollowed {username}"}, status=HTTP_200_OK)

class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = []
        for followed_user in following_users:
            posts.extend(followed_user.user_posts.all(order_by = 'created_at'))  
        return Response({"posts": posts}, status=HTTP_200_OK)