from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from django.contrib.auth.views import login

urlpatterns = [
    # the ones related to the login app
    url(r'^admin/', include(admin.site.urls)),
    url(r'^youtube/', include('youtubeplayer.urls')),
]