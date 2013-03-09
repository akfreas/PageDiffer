from django.conf.urls import patterns, include, url


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
     url(r'^incoming_sms', 'incoming_sms'),
     url(r'^admin/', include(admin.site.urls)),
)
