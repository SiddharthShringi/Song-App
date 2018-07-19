from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='songs')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=30)
    song = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
