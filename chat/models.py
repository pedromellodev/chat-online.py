from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    title = models.Charfield(max_length=200)
    messages = models.ManyToManyField('message')
    created_at = models.DateTimeField(auto_now_add=True)
    