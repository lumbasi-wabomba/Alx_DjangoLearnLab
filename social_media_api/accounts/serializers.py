from rest_framework import serializers
from .models import User, Comment
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'followers']

   

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            return {'user': user}
        raise serializers.ValidationError("Invalid credentials")
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # get_user_model().objects.create()
        # Token.objects.create(user=user)
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            bio = validated_data['bio'],
            profile_picture = validated_data['profile_picture']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

    def validate(self, attrs):
        user = self.context['request'].user
        if user.username != attrs['username']:
            raise serializers.ValidationError("You can only edit your own profile.")
        return attrs
    
