from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^mensualidades/(?P<username>[\w_-]+)$', v.MensualidadList.as_view(paginate_by=10), name="mensualidad_list"),
    url(r'^mensualidades/(?P<username>[\w_-]+)/suma$', v.MensualidadListSuma.as_view(), name="mensualidad_list_suma"),
    url(r'^mensualidades/(?P<username>[\w_-]+)/graph$', v.MensualidadListGraph.as_view(), name="mensualidad_list_graph"),
)
