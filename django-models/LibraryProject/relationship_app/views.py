from django.shortcuts import render
from django.views.generic import FormView  
from django.views.generic import RedirectView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Book
from .models import Library

from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

def function_based_view_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'book_list': books})

class LibraryDetailview(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def display_books(request):
        library_details = Library.objects.get(name= request)
        for library_detail in library_details:
            print(library_detail.title)

class LoginView(FormView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
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

@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
