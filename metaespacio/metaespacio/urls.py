from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^plantilla/', include('plantilla.urls')),
    url(r'^registro/', include('registro.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^biblioteca/', include('bibliotheca.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^informacion/$', TemplateView.as_view(template_name='informacion.html')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^', include('plantilla.urls')),
)
