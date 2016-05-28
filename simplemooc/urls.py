from django.conf.urls import include, url
from django.contrib import admin
from simplemooc.core.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),	
    url(r'^contact/$', 'simplemooc.core.views.contact', name='contact'),
    url(r'^$', 'simplemooc.core.views.home', name='home'),
]
