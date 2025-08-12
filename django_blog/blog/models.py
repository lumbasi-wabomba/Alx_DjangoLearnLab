from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=200, db_index=True, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    GENDER_CHOICES =[
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    bio = models.TextField()

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return f"post: {self.title} ; posted on: {self.published_date}"
