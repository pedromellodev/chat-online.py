from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length=200)
    messages = models.ManyToManyField('message')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)