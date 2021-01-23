
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Calendar.urls")),
    path('login/', include("login.urls")),
    path('', include('pwa.urls')),
   
]

urlpatterns += staticfiles_urlpatterns() 
