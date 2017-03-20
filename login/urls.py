from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_playlist/$', views.create_playlist, name='create_playlist'),
    url(r'^(?P<playlist_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<playlist_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<playlist_id>[0-9]+)/delete_album/$', views.delete_playlist, name='delete_playlist'),
    url(r'^(?P<playlist_id>[0-9]+)/add_preferences/$', views.add_preferences, name='add_preferences'),
]
