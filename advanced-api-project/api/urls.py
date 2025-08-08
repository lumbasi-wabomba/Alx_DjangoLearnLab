from django.urls import path
from .views import ListView
from .views import DetailView
from .views import CreateView
from .views import UpdateView
from .views import DeleteView


urlpatterns = [
    path('books/', ListView.as_view(), name='list-books'), 
    path('books/<int:pk>/', DetailView.as_view(), name='list-detailed-books'),
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/update/<int:pk>', UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>', DeleteView.as_view(), name='delete-book'),
]