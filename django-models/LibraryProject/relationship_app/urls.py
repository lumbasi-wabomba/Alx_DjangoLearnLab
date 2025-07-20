from django.contrib import admin
from django.urls import path
from relationship_app import views
from relationship_app.views import LibraryDetailview  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.function_based_view_book, name='books'),
    path('library/<int:pk>/', LibraryDetailview.as_view(), name='library'),  # Detail view
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
