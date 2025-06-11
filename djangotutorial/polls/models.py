from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='users/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='users/', null=True, blank=True)
    image_large = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # Додаємо зображення
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


