from django.conf.urls import patterns, include, url
from django.views.generic import *
from truck.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    # url(r'^trucks/', include('trucks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^trucks/$', truckList),
	url(r'^trucks/(?P<slug>[-_\w]+)/$', truckDetail),
	url(r'^contact/$', contactForm),
)
