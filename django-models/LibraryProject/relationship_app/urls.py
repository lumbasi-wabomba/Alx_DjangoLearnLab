from django.contrib import admin
from django.urls import path
from relationship_app import views
from relationship_app.views import Library_view
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('books/', views.function_based_view_book, name='books'),
     path('library/', Library_view.as_view(), name='library'),

]