# -*- coding: utf-8 -*-

from calendar import monthrange
from collections import OrderedDict
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from graphos.sources.simple import SimpleDataSource
from espacios.views import SiteMixin
from .gchart import ComboChart
from .models import Mensualidad


def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, monthrange(year, month)[1])
    return date(year, month, day)


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
        columnas = list(self.espacio.formapago_set.all().order_by('posicion'))
        columnas_dict = {x.pk: i for i, x in enumerate(columnas)}
        n = len(columnas) + 1 + 1 # + total liquido + total 
        zeros = [0.0] * n
        sumas_mensuales = OrderedDict()
        for mensualidad in self.get_queryset():
            key = mensualidad.pago.forma_pago.pk
            columna = columnas_dict[key]
            mes = mensualidad.fecha.replace(day=1)
            if mes not in sumas_mensuales:
                sumas_mensuales[mes] = zeros[:]
            sumas_mensuales[mes][columna] += mensualidad.cantidad
            if mensualidad.pago.forma_pago.liquido:
                sumas_mensuales[mes][n-2] += mensualidad.cantidad
            sumas_mensuales[mes][n-1] += mensualidad.cantidad

        # Rellena de ceros los meses intermedios no pagados
        meses = sumas_mensuales.keys()
        for i, mes in enumerate(meses):
            if i < len(meses)-1:
                mdelta = monthdelta(meses[i], meses[i+1])
                if mdelta > 1:
                    for m in range(1, mdelta):
                        new = add_months(mes, m)
                        sumas_mensuales[new] = zeros[:]
        sumas_mensuales = OrderedDict(sorted(sumas_mensuales.items(), key=lambda t: t[0]))

        context['columnas'] = columnas
        context['sumas'] = sumas_mensuales
        return context


class MensualidadListGraph(MensualidadListSuma):

    bar_colors = [
        "#32CD32",  # lime green
        "#4169E1",  # royal blue
        "#FFA500",  # orange
        "#ADFF2F",  # greenyellow
    ]
    expenses_color = "#F08080"  # light coral

    def get_template_names(self):
        return ["cuotas/mensualidad_list_graph.html"]

    def get_context_data(self, **kwargs):
        context = super(MensualidadListGraph, self).get_context_data(**kwargs)
        data = []
        colors = []
        if context['columnas']:
            # Titulos de las barras
            threshold = u'Gastos fijos' if not context['usuario'] else u'Cuota mínima'
            data.append([u'Meses']+[x.nombre for x in context['columnas']]+[threshold])
            # Colores de las barras
            for i, x in enumerate(context['columnas']):
                if x.color != "" and not x.color is None:
                    colors.append(x.color)
                else:
                    colors.append(self.bar_colors[i % len(self.bar_colors)])
            colors.append(self.expenses_color)
        if context['sumas']:
            for k, x in context['sumas'].items():
                # Para marcar los gastos fijos y la cuota minima
                if context['usuario']:
                    # FIXME: Fijar la cuota minima aplicable a su correspondiente mes
                    #   Por ahora cuota minima fija a 10.0
                    expenses = 9.95  # -0.05 para solapar la linea
                else:
                    # FIXME: Fijar gastos variables por cada mes
                    #   Por ahora gastos fijos de 300.0
                    expenses = 300.0
                # Datos de las mensualidades
                data.append([str(k.strftime('%b / %Y'))] + x[:-2] + [expenses])
        print(data)

        # Construye la grafica
        options = {
            'title': 'Mensualidades',
            'orientation': 'vertical',
            'isStacked': True,
            'colors': colors,
            'vAxis': {'title': 'Meses'},
            'seriesType': 'bars',
            'series': {len(colors)-1: {'type': 'steppedArea'}},
        }
        chart = ComboChart(SimpleDataSource(data=data), width="100%;",
                           height="auto;", options=options)
        context['chart'] = chart
        return context


class MensualidadListGeneralGraph(MensualidadListGraph):
    def get_template_names(self):
        return ["cuotas/mensualidad_list_suma.html"]
