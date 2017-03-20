from django.contrib.auth.models import Permission, User
from django.db import models


class Playlist(models.Model):
    user = models.ForeignKey(User, default=1)
    Plalyst_title = models.CharField(max_length=500,default='Default')

    def __str__(self):
        return self.Plalyst_title


class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

class AddPreferences(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    preferences = models.CharField(max_length=250)

    def __str__(self):
        return self.preferences
