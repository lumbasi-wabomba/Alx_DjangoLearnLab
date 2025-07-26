from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')