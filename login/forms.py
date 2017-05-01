from django import forms
from django.contrib.auth.models import User
from .models import Playlist,Song,AddPreferences

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['Plalyst_title']

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title']

class AddPreferencesForm(forms.ModelForm):

    class Meta:
        model= AddPreferences
        fields= ['preferences']

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
