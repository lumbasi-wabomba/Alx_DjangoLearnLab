from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
# Create your views here.

class ListView(generics.ListAPIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends =[filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
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