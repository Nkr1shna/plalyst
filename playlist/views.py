from django.shortcuts import render
import psycopg2

try:
    conn = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='localhost' password='musicbrainz'")
except:
    print ("I am unable to connect to the database");

def generate_song(request):
    cur = conn.cursor()
    cur.execute("""Select distinct t.name from track t join artist_credit ac on t.artist_credit = ac.id join artist_credit_name acn
                on ac.id = acn.artist_credit
                join artist a
                on acn.artist = a.id
                where a.name='Linkin Park'""")
    rows = cur.fetchall()
    return render(request, 'generated.html', {'artists': rows})