from django.conf.urls import include, url
from django.contrib import admin
from simplemooc.core.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),	
    url(r'$^', home, name='home')

]
