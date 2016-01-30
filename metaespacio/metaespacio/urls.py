from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^registro/', include('registro.urls')),
    url(r'^cuotas/', include('cuotas.urls')),
    url(r'^encuestas/', include('encuestas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^espacios/', include('espacios.urls')),
    url(r'^contabilidad/', include('contabilidad.urls')),
    # url(r'^biblioteca/', include('bibliotheca.urls')),
    # url(r'^api/', include('bibliotheca.api_urls)),
    url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^', include('pages.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
