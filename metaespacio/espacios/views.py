# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.views.generic import ListView
from .models import Miembro


class SiteMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.site = get_current_site(request)
        # FIXME espacio-site debe ser un 1to1 no un fk
        self.espacio = self.site.espacio_set.first()
        if request.user.is_authenticated():
            self.miembro = Miembro.objects.filter(
                user=request.user, espacio=self.espacio).first()
        else:
            self.miembro = None
        return super(SiteMixin, self).dispatch(request, *args, **kwargs)


class MemberOnly(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.miembro:
            raise Http404
        return super(MemberOnly, self).dispatch(request, *args, **kwargs)


class AdminOnly(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(AdminOnly, self).dispatch(request, *args, **kwargs)


class FilterEspacioSiteMixin(SiteMixin):
    def get_queryset(self):
        return super(FilterEspacioSiteMixin, self).get_queryset().filter(espacio__site=self.site)


class ListMember(FilterEspacioSiteMixin, ListView):
    model = Miembro
