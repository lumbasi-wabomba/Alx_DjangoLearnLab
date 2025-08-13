from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(User):
    bio = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return f"post: {self.title} ; posted on: {self.published_date}"
    
    
