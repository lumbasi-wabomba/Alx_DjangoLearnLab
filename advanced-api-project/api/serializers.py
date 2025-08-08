from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    model = Book
    fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    model = Author
    fields = ['name']
    book = BookSerializer(many=True, read_only=True)

    
    def validate_publication_year(self, data):
        if date().year(data['publication_year']) > date.today().year(): 
            raise serializers.ValidationError("the date is in the future")
        return data
