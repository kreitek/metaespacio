# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', v.EncuestaView.as_view(), name="encuesta_view"),
)
