# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import Mensualidad
from espacios.views import SiteMixin
from collections import OrderedDict
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import BarChart


class MensualidadList(SiteMixin, ListView):
    model = Mensualidad

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/')
        return super(MensualidadList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        kwargs = {"miembro__espacio__site": self.site}
        username = self.kwargs.get('username')
        if username:
            url_user = get_object_or_404(User, username=username)
            kwargs["miembro__user"] = url_user
        user = self.request.user
        if self.espacio not in user.espacio_set.all():
            raise Http404
        return super(MensualidadList, self).get_queryset().filter(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(MensualidadList, self).get_context_data(**kwargs)
        context['usuario'] = self.kwargs.get('username')
        return context


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

        context['columnas'] = columnas
        context['sumas'] = sumas_mensuales
        return context


class MensualidadListGraph(MensualidadListSuma):
    def get_template_names(self):
        return ["cuotas/mensualidad_list_graph.html"]
      
    def get_context_data(self, **kwargs):
        context = super(MensualidadListGraph, self).get_context_data(**kwargs)
        data = []
        if context['columnas']: 
            data.append([u'Meses']+[x.nombre for x in context['columnas']])
        if context['sumas']:
            for k, x in context['sumas'].items():
                data.append([str(k.strftime('%b / %Y'))] + x[:-1])
        print(data)
        chart = BarChart(SimpleDataSource(data=data), width="100%;", \
            height="auto;", options={'isStacked': True, 'title': 'Mensualidades', \
            "colors": ["#32CD32", "#4169E1", "#FFA500"], 'vAxis': {'title': 'Meses'}})
        context['chart'] = chart
        return context

class MensualidadListGeneralGraph(MensualidadListGraph):
    def get_template_names(self):
        return ["cuotas/mensualidad_list_suma.html"]
