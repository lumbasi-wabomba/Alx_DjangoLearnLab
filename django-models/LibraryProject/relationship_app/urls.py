from django.contrib import admin
from django.urls import path
from relationship_app import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.function_based_view_book, name='books'),
    path('library/', Library_view.as_view(), name='library'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),


]