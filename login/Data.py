from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from random import randint
import MySQLdb



class RegisterDetails():
    def __init__(self):
        self.name=get_random_string(length=10)
        self.email=self.name+"@gmail.com"
        self.password=User.objects.make_random_password(length=10, allowed_chars='123456789')

class UserData():
    def __init__(self, username, password):
        self.name=username
        self.password=password

def LoginData():
    username="manmitha"
    password="kc433"
    user=UserData(username,password)
    return user

def LoginDataGenerate():
    username="kr1shna"
    password="40OZlike"
    user=UserData(username,password)
    return user


def PlaylistName():
    namelist=['rock','pop','classical','country','metal']
    randomNum=randint(0, 4)
    return namelist[randomNum]

def inputSong():
    conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
    cur = conn1.cursor()
    cur.execute('select name from Song order by id asc limit 8')
    songsList = cur.fetchall()
    inputByUser = []
    for song in songsList:
        inputByUser.append(song[0])
    return inputByUser

