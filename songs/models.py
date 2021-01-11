from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Song(models.Model):
    title=models.CharField(max_length=64)
    lyrics = models.TextField()
    publisher =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

