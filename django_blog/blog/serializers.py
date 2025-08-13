
from .models import Post, User
from rest_framework import serializers
from datetime import date

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['title', 'content', 'published_date', 'author']
        read_only_fields = ['published_date', 'author']

    def validate(self, value):
        if value < date.today():
            raise serializers.ValidationError("published date is invalid")
        return value    
    

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    

    