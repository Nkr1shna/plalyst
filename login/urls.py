from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from . import views



urlpatterns = [
    url(r'^$',login),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
]
