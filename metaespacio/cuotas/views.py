# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Mensualidad
from espacios.views import SiteMixin
from collections import OrderedDict


class MensualidadList(SiteMixin, ListView):
    model = Mensualidad

    def get_queryset(self):
        url_user = get_object_or_404(User, username=self.kwargs['username'])
        login_user = self.request.user
        if not login_user.is_superuser and url_user.pk != login_user.pk:
            raise Http404
        return super(MensualidadList, self).get_queryset().filter(
            miembro__user=url_user,
            miembro__espacio__site=self.site)


class MensualidadListSuma(MensualidadList):
    def get_template_names(self):
        return ["cuotas/mensualidad_list_suma.html"]

    def get_context_data(self, **kwargs):
        context = super(MensualidadListSuma, self).get_context_data(**kwargs)
        columnas = list(self.espacio.formapago_set.all())
        columnas_dict = {x.pk: i for i, x in enumerate(columnas)}
        n = len(columnas) + 1
        zeros = [0.0] * n
        sumas_mensuales = OrderedDict()
        for mensualidad in self.get_queryset():
            key = mensualidad.pago.forma_pago.pk
            columna = columnas_dict[key]
            mes = mensualidad.fecha.replace(day=1)
            if mes not in sumas_mensuales:
                sumas_mensuales[mes] = zeros[:]
            sumas_mensuales[mes][columna] += mensualidad.cantidad
            sumas_mensuales[mes][n-1] += mensualidad.cantidad

        context['usuario'] = self.kwargs['username']
        context['columnas'] = columnas
        context['sumas'] = sumas_mensuales
        return context


class MensualidadListGraph(MensualidadListSuma):
    def get_template_names(self):
        return ["cuotas/mensualidad_list_graph.html"]
