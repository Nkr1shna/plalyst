from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^', include('login.urls')),
    url(r'^youtube/', include('youtubeplayer.urls')),
    url(r'^generate/', include('playlist.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)