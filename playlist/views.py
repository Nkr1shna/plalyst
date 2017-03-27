from django.shortcuts import render
import psycopg2
from login.models import Playlist,Song
from django.db.models import Q
from django.db import models

try:
    conn = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='localhost' password='musicbrainz'")
except:
    print ("I am unable to connect to the database");

def generate_song(request):
    cur = conn.cursor()
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        playlists = Playlist.objects.filter(user=request.user)
        songs = Song.objects.filter(playlist=playlists.first())
        cur.execute("""Select a.name from track t join artist_credit ac on t.artist_credit = ac.id join artist_credit_name acn
                on ac.id = acn.artist_credit
                join artist a
                on acn.artist = a.id
                where t.name= %s group by a.name order by count(a.name) desc limit 1""",(songs[1].song_title.title(),))
        rows = cur.fetchall()
        return render(request, 'generated.html', {'artists': rows})