from django.conf.urls import url,include
from . import views
from login.views import index

app_name = 'login'

urlpatterns = [
    url(r'^$', views.generate_playlist, name='generate'),
]