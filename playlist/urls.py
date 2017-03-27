from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.generate_song, name='generate'),
]