from django.conf.urls import patterns, include, url
import django


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PageDiffer.views.home', name='home'),
     url(r'^differ/', include('Differ.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


     url(r'^admin/', include(admin.site.urls)),
)

