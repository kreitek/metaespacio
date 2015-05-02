# -*- coding: utf-8 -*-
from django.views.generic import ListView
from .models import Mensualidad
from espacios.views import SiteMixin


class MensualidadList(SiteMixin, ListView):
    model = Mensualidad

    def get_queryset(self):
        return super(MensualidadList, self).get_queryset().filter(
            miembro__user=self.request.user,
            miembro__espacio__site=self.site)
