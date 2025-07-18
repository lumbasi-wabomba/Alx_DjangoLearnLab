from django.shortcuts import render
from django.http import HttpResponse
from .models import Author 
from .models import Librarian
from .models import Library
from .models import Book
from django.views.generic import DetailView

def function_based_view_book(request):
    books = Book.objects.all()
    context ={'book_list': books}
    return render(request, 'LibraryProject/templates/relationship_app/book_list.html', context)
# Create your views here.
class Library_view(DetailView):
    model = Library
    template = 'library/library_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        return context


