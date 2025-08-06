from django.urls import path
from django.urls import include
from .views import BookList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books_all', BookList, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('', include(router.urls)),
]

