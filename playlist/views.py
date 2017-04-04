from django.shortcuts import render
import psycopg2
from login.models import Playlist
from song.models import *
from django.db.models import Q
from django.db import models
import random
import sys
import sqlite3

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


def migrateDB(request):
    success=0
    try:
        conn = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='localhost' password='musicbrainz'")
        conn1 = sqlite3.connect('db.sqlite3')
        conn2 = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur1 = conn1.cursor()
        cur2 = conn2.cursor()
        rnumbers = random.sample(range(1, 22660511), 100000)
        for eachnum in rnumbers:

            cur.execute("""select name from track where id =%d""", (eachnum,))
            rows = cur.fetchall()
            songName = rows[0][0]
            cur1.execute("INSERT INTO Song VALUES (?)",songName)
            cur.execute("""select distinct t.name from track tr
                join recording r
                on tr.recording = r.id
                join recording_tag rt
                on rt.recording = r.id
                join tag t
                on
                rt.tag= t.id
                where tr.name = %s
                order by t.name""", (rows[0][0],))
            rows = cur.fetchall()
            for row in rows:
                cur2.execute("select * from Tag where name=?",row[0]) #exexute and see!!!!
                row2 = cur2.fetchall()
                if (row2.count()==0):
                    cur1.execute("INSERT INTO Tag VALUES (?)", row[0])
                cur2.execute("select id from Song where name =?",songName)
                songId = cur2.fetchall()[0][0]
                cur2.execute("select id from Tag where name =?", row[0])
                tagId = cur2.fetchall()[0][0]
                cur2.execute("Insert into SongTag VALUES (?,?)",songId,tagId)
        cur.close()
        cur1.close()
        cur2.close()
        conn.close()
        conn1.close()
        conn2.close()
        success = "done"


    except:
        e = sys.exc_info()[0]
        success= e;

    return render(request, 'generated.html', {'artists': success})
