import MySQLdb
import csv
from login.Commontests import GenerateSongsTest,GenerateSongsTestDiff
from .Parser import file


conn1 = MySQLdb.connect(host = "localhost", user = "root", passwd = "40OZlike", db = "plalyst")
cur = conn1.cursor()
conn1.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
cur.execute("insert into login_playlist (Plalyst_title,user_id) values('test_pl',1)")
cur.execute("commit")
cur.execute("select id from login_playlist where Plalyst_title= 'test_pl'")
pl_id = cur.fetchall()[0][0]
with open('TestLibrary/'+file, 'rt',encoding='UTF-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
    for row in spamreader:
        curry = 'insert into login_song (song_title,playlist_id) values("'+row[0]+'",'+str(pl_id)+')'
        print(curry)
        cur.execute(curry)
        cur.execute("commit")
cur.close()
conn1.close()

