
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
