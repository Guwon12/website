# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='movies/')
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
