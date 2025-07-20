from django.shortcuts import render
from django.views.generic import DetailView, FormView, RedirectView
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Author, Librarian, Library, Book

# ✅ Function-based view to list all books
def function_based_view_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'book_list': books})

# ✅ Class-based detail view for Library
class LibraryDetailview(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.get_object()
        return context

# ✅ Class-based Login view
class LoginView(FormView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super().form_valid(form)

# ✅ Class-based Logout view
class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(request, *args, **kwargs)

# ✅ Class-based Register view
class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)

# ✅ Profile view for logged-in users
@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html')
