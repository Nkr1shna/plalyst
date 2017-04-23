from django.conf.urls import url,include
from . import views
from login.views import index

app_name = 'playlist'

urlpatterns = [
    url(r'^$', views.generate_playlist, name='generate'),
    url(r'(?P<song_name>.+)/$', views.generate_playlist, name='youtube'),
]