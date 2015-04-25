# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site


class FilterEspacioSiteMixin(object):
    def get_queryset(self):
        all = super(FilterEspacioSiteMixin, self).get_queryset()
        site = get_current_site(self.request)
        return all.filter(espacio__site=site)
