from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^plantilla/', include('plantilla.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
