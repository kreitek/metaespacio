from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^mensualidades/$', v.MensualidadListGeneralGraph.as_view(),
        name="mensualidad_resumen"),
    url(r'^mensualidades/pagos$', v.MensualidadList.as_view(),
        name="mensualidad_pagos"),
    url(r'^mensualidades/(?P<username>[\w_-]+)/$',
        v.MensualidadListGeneralGraph.as_view(), name="mensualidad_resumen"),
    url(r'^mensualidades/(?P<username>[\w_-]+)/pagos$', v.MensualidadList.as_view(
        paginate_by=10), name="mensualidad_pagos"),
    #url(r'^mensualidades/(?P<username>[\w_-]+)/graph$',
    #    v.MensualidadListGraph.as_view(), name="mensualidad_list_graph"),
)
