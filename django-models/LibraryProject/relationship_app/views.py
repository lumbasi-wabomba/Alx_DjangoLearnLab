from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Librarian, Library, Book
from django.views.generic import DetailView, FormView , RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy


# View to list all books
def function_based_view_book(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based detail view for Library
class LibraryDetailview(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['library'] = library 
        return context

class LoginView(FormView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super().form_valid(form)

class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(request, *args, **kwargs)

class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)



# Auth views
@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html')
