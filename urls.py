from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import simple
from django.conf import settings
import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
       (r'media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }))
