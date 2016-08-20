"""MyTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from MyTravel.views import *
from itinerary.views import *
from django.conf.urls.static import static

urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_page, name='homepage'),
    url(r'^about/$', about_page, name='about_page'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^post/(?P<station_id>\d+)/$', post_page, name='post_page'),

    url(r'^event/add/(?P<station_id>\d+)/$', event_add, name='event_add'),
    url(r'^event/edit/(?P<event_id>\d+)/$', event_edit, name='event_edit'),

    url(r'^station/edit/(?P<station_id>\d+)/$', station_edit, name='station_edit'),
    url(r'^station/add/$', station_add, name='station_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
