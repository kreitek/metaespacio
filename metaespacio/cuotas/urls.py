from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^mensualidades/(?P<username>\w+)$', v.MensualidadList.as_view(), name="mensualidad_list"),
)
