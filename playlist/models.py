from django.db import models


class Song(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'Song'


class Songtag(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, db_column='song', blank=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='tag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SongTag'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tag'

