from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Librarian, Library, Book
from django.views.generic import DetailView

def function_based_view_book(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class Library_view(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library'] = library 
        return context
