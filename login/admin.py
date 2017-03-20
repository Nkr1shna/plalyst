from django.contrib import admin
from .models import Playlist,Song,AddPreferences

admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(AddPreferences)