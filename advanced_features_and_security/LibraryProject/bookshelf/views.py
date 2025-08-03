from django.shortcuts import render

# Create your views here.
# library/views.py
from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm
from django.db.models import Q
#from django.shortcuts import render
#from .models import Book


@login_required
@permission_required('library.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
@permission_required('library.can_create', raise_exception=True)
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form})

@login_required
@permission_required('library.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form})

@login_required
@permission_required('library.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# views.py (search view - secure)

def book_search(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return render(request, 'library/book_search.html', {'results': results, 'query': query})

form = BookSearchForm(request.GET)
if form.is_valid():
    query = form.cleaned_data['query']
    results = Book.objects.filter(title__icontains=query)
