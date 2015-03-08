from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cal/', 'www.views.cal', name='cal'),
    url(r'', 'www.views.home', name='home'),
)
