from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username

class Comment(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    tags = models.ManyToManyField(User)

    def __str__(self):
        return self.post
    
    