import psycopg2
import random

try:
    conn = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='localhost' password='musicbrainz'")
    conn1 = psycopg2.connect("dbname='plalyst' user='musicbrainz' host='localhost' password='musicbrainz'")
    conn2 = psycopg2.connect("dbname='plalyst' user='musicbrainz' host='localhost' password='musicbrainz'")
    print("connections made...")
    cur = conn.cursor()
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    print("cursors created....")
    print("table created")        
    rnumbers = random.sample(range(1, 22660511), 100000)
    print("Random numbers generated...")
    for eachnum in rnumbers:
        print(eachnum)
        songName=""
        while(songName==""):
            cur.execute("""select name from track where id = %s """, (eachnum,))
            rows = cur.fetchall()
            print(rows)
            if not len(rows)==0:
                songName = rows[0][0]
            eachnum+=1
        print("Got the track name:")
        print(songName)
        sql = 'INSERT into Song values (NULL, "'+songName+'")'
        print(sql)
        cur1.execute(sql)
        print("inserted into the song table....")
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
        print("got the tag names....")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            qry = "select * from Tag where name='"+row[0]+"'"
            print(qry)
            cur2.execute(qry)
            row2 = cur2.fetchall()
            print("getting if the tag is already in")
            if (len(row2)==0):
                qry1 = "INSERT INTO Tag VALUES (NULL,'"+row[0]+"')"
                print(qry1)
                cur1.execute(qry1)
                print("inserted into the tag table..")
            qry2 = "select id from Song where name='"+songName+"'"
            cur2.execute(qry2)
            mi= cur2.fetchall()
            print(mi)
            songId = mi[0][0]
            qry3 = "select id from Tag where name='"+row[0]+"'"
            cur2.execute(qry3)
            tagId = cur2.fetchall()[0][0]
            qry1 = "INSERT INTO SongTag VALUES ('"+songId+"','"+tagId+"')"
            cur2.execute(qry4)
            print("inserted into the songtag table..")
    cur.close()
    cur1.close()
    cur2.close()
    conn.close()
    conn1.close()
    conn2.close()
except:
    print(e)