from .models import Post, User
from .serializers import UserSerializer, PostSerializer
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from django.forms import ModelForm
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



class LoginView(ModelForm):
    serializer_class = UserSerializer
    look_field = 'username'
    authentication_classes = [TokenAuthentication]

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def logout(self, request):
        request.auth.delete()
        return Response({"message": "Logged out successfully"}, status=200)
    
class RegisterView(UserCreationForm):
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        return Response(serializer.errors, status=400)
    
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    

    