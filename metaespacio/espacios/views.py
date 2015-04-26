# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site


class SiteMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.site = get_current_site(request)
        return super(SiteMixin, self).dispatch(request, *args, **kwargs)

class FilterEspacioSiteMixin(SiteMixin):
    def get_queryset(self):
        return super(FilterEspacioSiteMixin, self).get_queryset().filter(espacio__site=self.site)
