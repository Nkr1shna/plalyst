from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from django.contrib.auth.views import login

urlpatterns = [
    # the ones related to the login app
    url(r'^$', include('login')),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', include('login')),  # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ytp/$', include('youtubeplayer.urls')),
]