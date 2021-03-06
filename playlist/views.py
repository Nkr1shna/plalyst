from django.shortcuts import render
import MySQLdb
import numpy as np
import math
import re
import urllib.parse



def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


def generate_playlist(request, playlist_id='', song_name=''):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur= conn1.cursor()
        class Song:
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
        sngQry = 'select song_title from login_song where playlist_id = '+playlist_id
        cur.execute(sngQry)
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
        prefQry = 'select id from Tag where name in (select preferences from login_addpreferences where playlist_id = '+playlist_id+')'
        cur.execute(prefQry)
        prefren = cur.fetchall()
        preflist = []
        for pref in prefren:
            preflist.append(str(pref[0]))
        preflist=list(set(preflist))
        if(len(preflist)==0):
            preflist= '100090877687'
        else:
            preflist = ",".join(preflist)

        sql = 'select distinct Song.name, Song.id from Song join SongTag on SongTag.song = Song.id where SongTag.tag in ('+tagList+') and Song.name not in ('+inputByUser+') and SongTag.tag not in ('+preflist+')'
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
        if song_name == '':
            song_name = recommended30[0].name
        link = generate_youtube(song_name)
        return render(request, 'generated.html', {'recommended30': recommended30, 'yt_link': link, 'playlist_id' : playlist_id}, )


def generate_youtube(song_name):
    query_string = urllib.parse.urlencode({"search_query": song_name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    link = "http://www.youtube.com/embed/" + search_results[0];
    return link