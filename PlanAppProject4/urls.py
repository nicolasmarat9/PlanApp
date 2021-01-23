
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Calendar.urls")),
    path('login/', include("login.urls")),
    path('', include('pwa.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),     
]

urlpatterns += staticfiles_urlpatterns() 
