from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListView(generics.ListAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Book.objects.all()
    serializer_class = BookSerializer