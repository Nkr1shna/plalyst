from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

# Check song exists methods
# - checks if the songs is present in the database
# -if present it allows the user to add the next song