from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from dateutil.relativedelta import relativedelta
import datetime
from espacios.views import SiteMixin, MemberOnly
from .models import Linea, Cuenta


class LineaList(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        # la busqueda por fecha es lo que ha generado usar objetos Q
        query = Q(cuenta__espacio__site=self.site)

        # Esto es para poner las cosas que nos piden que busquen
        self.filters = {}

        # busqueda por cuenta
        cuenta = self.request.GET.get('cuenta')
        if cuenta:
            query &= Q(cuenta__nombre=cuenta)
            self.filters['cuenta'] = cuenta

        # busqueda por usuario
        usuario = self.request.GET.get('usuario')
        if usuario:
            query &= Q(miembro__user__username=usuario)
            self.filters['usuario'] = usuario

        # busqueda por mensualidad mm/yyyy
        mensualidad = self.request.GET.get('mensualidad', '')
        try:
            mensualidad = datetime.datetime.strptime(mensualidad, "%m/%Y").date()
        except ValueError:
            mensualidad = None
        if mensualidad:
            mensualidad_ini = mensualidad.replace(day=1)
            mensualidad_fin = mensualidad_ini + relativedelta(months=1, days=-1)
            Q1 = Q(fecha__isnull=False, fecha__gte=mensualidad_ini, fecha__lte=mensualidad_fin)
            Q2 = Q(fecha__isnull=True, asiento__fecha__gte=mensualidad_ini, asiento__fecha__lte=mensualidad_fin)
            query &= (Q1 | Q2)
            self.filters['mensualidad'] = mensualidad

        # lets go
        return super(LineaList, self).get_queryset().filter(query).order_by('fecha')

    def get_context_data(self, **kwargs):
        context = super(LineaList, self).get_context_data(**kwargs)
        context['filters'] = self.filters
        return context


class LineasUsuario(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        kwargs = {"miembro__espacio__site": self.site}
        username = self.kwargs.get('username')
        if username:
            url_user = get_object_or_404(User, username=username)
            kwargs["miembro__user"] = url_user
        return super(LineasUsuario, self).get_queryset().filter(**kwargs).order_by('fecha')

    def get_context_data(self, **kwargs):
        context = super(LineasUsuario, self).get_context_data(**kwargs)
        context['titulo'] = self.kwargs.get('username')
        return context


class LineasCuenta(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        self.cuenta = get_object_or_404(Cuenta, espacio=self.espacio, pk=self.kwargs['pk'])
        return super(LineasCuenta, self).get_queryset().filter(cuenta=self.cuenta).order_by('fecha')

    def get_context_data(self, **kwargs):
        context = super(LineasCuenta, self).get_context_data(**kwargs)
        context['titulo'] = self.cuenta
        return context


class CuentasList(SiteMixin, MemberOnly, ListView):
    model = Cuenta
