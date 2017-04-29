from django.conf.urls import url,include
from . import views
from login.views import index

app_name = 'playlist'

urlpatterns = [
    url(r'^(?P<playlist_id>[0-9]+)/$', views.generate_playlist, name='generate'),
    url(r'^(?P<playlist_id>[0-9]+)/(?P<song_name>.+)/$', views.generate_playlist, name='youtube'),
    url(r'^(?P<playlist_id>.*)/(?P<song_name>.+)/$', views.generate_playlist, name='youtube'),
]