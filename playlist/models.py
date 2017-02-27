from django.db import models
from song.models import Song


# Create your models here.

class PlaSongs(models.Model):
    plalysts_id = models.ForeignKey('''after creating plalysts model''')
    song_id = models.ForeignKey('''After creating song model''')

def generate_song():
    return 0
    #dummy method

def add_to_plalyst(pid,sid):
    plasongs_obj = PlaSongs(plalyst_id=pid,song_id=sid)
    plasongs_obj.save()
    return 0
    #dummy method

#takes the plalyst_id ,song_id and the operation(delete the song or plalyst)
def modify_plalyst(pid,sid,op):
    return 0

#takes the songs name and plays it on youtube
def play_via_youtube(sid):
    song= Song.objects.filter(id = sid)

