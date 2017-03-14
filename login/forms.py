from django import forms
from django.contrib.auth.models import User
from .models import Album

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['Plalyst_title']
