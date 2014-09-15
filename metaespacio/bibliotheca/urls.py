#!/usr/bin/env python
# -*- coding: utf-8 -*-
# urls for bibliotheca/metaspacio 
#

from django.conf.urls import *
from .views import LastestBooks

urlpatterns = patterns('bibliotheca.views',
    url(r'^$', LastestBooks.as_view()),
    )

