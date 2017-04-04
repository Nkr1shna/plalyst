from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=200)


# Check song exists methods
# - checks if the songs is present in the database
# -if present it allows the user to add the next song

class Tag(models.Model):
    name = models.CharField(max_length=200)


class SongTag(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


