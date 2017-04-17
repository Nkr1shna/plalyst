from django.shortcuts import render
from login.models import Playlist
from song.models import *
from django.db.models import Q
from django.db import models
import MySQLdb
import numpy as np
import math

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def generate_playlist(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        conn1 = MySQLdb.connect(host = "localhost", user = "root", passwd = "40OZlike", db = "plalyst")
        cur= conn1.cursor()
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
                self.cosineTag =[]
                j = 0;
                for inpSong in songList:
                    tagList = list(self.tags)
                    tagList.extend(inpSong.tags)
                    tagList = list(set(tagList))
                    inpMatrix = []
                    retMatrix = []
                    for i in range(0,len(tagList)):
                        inpMatrix.append(inpSong.tags.count(tagList[i]))
                        retMatrix.append(self.tags.count(tagList[i]))
                    result = cosine_similarity(inpMatrix, retMatrix)
                    self.cosineTag.append(result)
                    j+=1
                self.avgCos = np.mean(self.cosineTag)

        cur.execute('select name from Song order by id desc limit 8')
        songs = cur.fetchall()
        songList = []
        inputByUser = []
        for songName in songs:
            inputByUser.append('"'+songName[0]+'"')
            s = Song(songName[0])
            songList.append(s)
        tagList = []
        for song in songList:
            for tag in song.tags:
                tagList.append(str(tag))
        tagList=list(set(tagList))
        tagList = ",".join(tagList)
        inputByUser=list(set(inputByUser))
        inputByUser = ",".join(inputByUser)
        sql = 'select distinct Song.name, Song.id from Song join SongTag on SongTag.song = Song.id where SongTag.tag in ('+tagList+') and Song.name not in ('+inputByUser+')'
        cur.execute(sql)
        recSongs = cur.fetchall()
        recSongList = []
        for recSongName in recSongs:
            r = RecommendedSong(recSongName[0],recSongName[1],songList)
            recSongList.append(r)
        recSongList.sort(key=lambda x: x.avgCos, reverse=True)
        cur.close()
        conn1.close()
        recommended30 = recSongList[:30]
        return render(request, 'generated.html', {'recommended30': recommended30})
