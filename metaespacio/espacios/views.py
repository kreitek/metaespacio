# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView
from .models import Miembro


class SiteMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.site = get_current_site(request)
        # FIXME espacio-site debe ser un 1to1 no un fk
        self.espacio = self.site.espacio_set.first()
        return super(SiteMixin, self).dispatch(request, *args, **kwargs)


class FilterEspacioSiteMixin(SiteMixin):
    def get_queryset(self):
        return super(FilterEspacioSiteMixin, self).get_queryset().filter(espacio__site=self.site)


class ListMember(FilterEspacioSiteMixin, ListView):
    model = Miembro
