from django.conf.urls.defaults import *
from views import login, register

urlpatterns = patterns('',
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register')
)
