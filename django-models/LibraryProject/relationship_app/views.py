from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from .models import Librarian
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

def function_based_view_book(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailview(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library'] = library 
        return context

@login_required
def profile_view(request):
    return render(request, 'relationship_app/profile.html')

def logout(request):
    return render(request, 'relationship_app/logout.html')

def login(request):
     return render(request, 'relationship_app/login.html')

def register(request):
     return render(request, 'relationship_app/register.html')