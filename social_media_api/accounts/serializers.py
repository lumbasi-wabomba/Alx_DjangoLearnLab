from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'following']
        read_only_fields = ['id', 'following']

   

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = CustomUser.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            return {'user': user}
        raise serializers.ValidationError("Invalid credentials")
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # get_user_model().objects.create_user()
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
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

    def validate(self, attrs):
        user = self.context['request'].user
        if user.username != attrs['username']:
            raise serializers.ValidationError("You can only edit your own profile.")
        return attrs