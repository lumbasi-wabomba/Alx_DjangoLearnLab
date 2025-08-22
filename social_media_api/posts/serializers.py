from .models import Post, Comment
from rest_framework import  serializers


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = '__all__'
    read_only_fields = ['created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("content cannot be empty")
        return value 

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = '__all__'
    read_only_fields = ['created_at', 'updated_at']

    def validate_post(self, value):
        if not value:
            raise serializers.ValidationError("the post is not available")
        return value


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)