from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^mensualidad$', v.MensualidadList.as_view(), name="mensualidad_list"),
)
