#Collect the tags from the songs from the user
#get all the songs with the tags
#Compute the cosine similarity with input songs
#compute the average of the similarity
#sort the similarities
#pick the highest 30
import MySQLdb
from scipy import spatial
import numpy as np

conn1 = MySQLdb.connect(host = "localhost", user = "root", passwd = "40OZlike", db = "plalyst")
cur= conn1.cursor()
print("connections and cursors made...")

class Song():
    def __init__(self, name):
        self.name = name
        cur.execute('select id from Song where name ="'+name+'"')
        self.id = cur.fetchall()[0][0]
        self.tags = []
        cur.execute('select tag from SongTag where song ="'+str(self.id)+'"')
        tags = cur.fetchall()
        for tag in tags:
            self.tags.append(tag[0])

class RecommendedSong():
    def __init__(self, name, id, songList):
        self.name = name
        self.id = id
        self.tags = []
        cur.execute('select tag from SongTag where song ="'+str(self.id)+'"')
        tags = cur.fetchall()
        for tag in tags:
            self.tags.append(tag[0])
        cosineTag =[]
        j = 0;
        for inpSong in songList:
            tagList = list(self.tags)
            tagList.extend(inpSong.tags)
            tagList = list(set(tagList))
            inpMatrix = []
            retMatrix = []
            for i in range(0,len(tagList)-1):
                print("The tag id is :")
                print(tagList[i])
                inpMatrix.append(inpSong.tags.count(tagList[i]))
                retMatrix.append(self.tags.count(tagList[i]))
            result = 1 - spatial.distance.cosine(inpMatrix, retMatrix)
            cosineTag.append(result)
            j+=1
        self.avgCos = np.mean(cosineTag)



cur.execute('select name from Song order by id desc limit 8')
songs = cur.fetchall()
songList = []
for songName in songs:
    s = Song(songName[0])
    songList.append(s)

tagList = []
for song in songList:
    print(song.tags)
    for tag in song.tags:
        tagList.append(str(tag))

tagList=list(set(tagList))
tagList = ",".join(tagList)
sql = 'select Song.name, Song.id from Song join SongTag on SongTag.song = Song.id where SongTag.tag in ('+tagList+')'
print(sql)
cur.execute(sql)
recSongs = cur.fetchall()
print(len(recSongs))
recSongList = []
for recSongName in recSongs:
    r = RecommendedSong(recSongName[0],recSongName[1],songList)
    recSongList.append(r)
recSongList.sort(key=lambda x: x.avgCos, reverse=True)

recommended30 = recSongList[:30]
for recS in recommended30:
    print(recS.name)
cur.close()
conn1.close()
