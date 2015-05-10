# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>.+)$', v.PaginaView.as_view(), name="pagina_view"),
    url(r'^$', v.PaginaIndex.as_view(), name="inicio"),
)
