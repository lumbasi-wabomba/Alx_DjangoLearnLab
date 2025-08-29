from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def create_notification(self, user, post):
        notification = Notification.objects.create(user=user, post=post)
        return notification
    
    def update_notification(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance
    def delete_notification(self, instance):
        instance.delete()

    def get_notifications(self, user):
        return Notification.objects.filter(user=user)

    def get_notification(self, user, post):
        return Notification.objects.filter(user=user, post=post).first()