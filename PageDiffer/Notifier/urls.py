from django.conf.urls import patterns, include, url
import django


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('Differ.views',
    # Examples:
    # url(r'^$', 'PageDiffer.views.home', name='home'),
    # url(r'^PageDiffer/', include('PageDiffer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$', 'index'),
     url(r'^incoming_sms', 'incoming_sms'),
     url(r'^send-info', 'capture_info'),
     url(r'^admin/', include(admin.site.urls)),
)

