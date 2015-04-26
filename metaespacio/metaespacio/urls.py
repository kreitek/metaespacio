from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^registro/', include('registro.urls')),
    url(r'^encuestas/', include('encuestas.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^biblioteca/', include('bibliotheca.urls')),
    # url(r'^api/', include('bibliotheca.api_urls)),
    url(r'^', include('common.urls')),
)
