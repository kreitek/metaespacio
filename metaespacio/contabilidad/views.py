from django.views.generic import ListView, TemplateView
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from dateutil.relativedelta import relativedelta
import collections
import datetime
from espacios.views import SiteMixin, MemberOnly, AdminOnly
from .models import Linea, Cuenta, Asiento


def objeto_q_linea_por_mes(mes):
    # Tenemos el problema de que las fechas en las lineas son opcionales y las fechas
    # en los asientos obligatorios. Esto es para hacer busquedas por fecha sobre
    # asientos. FIXME esto se puede meter como un manager en los modelos y queda
    # mejor.
    mes_ini = mes.replace(day=1)
    mes_fin = mes_ini + relativedelta(months=1, days=-1)
    Q1 = models.Q(fecha__isnull=False, fecha__gte=mes_ini, fecha__lte=mes_fin)
    Q2 = models.Q(fecha__isnull=True, asiento__fecha__gte=mes_ini, asiento__fecha__lte=mes_fin)
    return Q1 | Q2


def objeto_q_cuenta_por_mes(mes):
    # Es igual que el anterior agregando linea__ para hacer busquedas por fecha
    # sobre cuentas. FIXME idem meter en un manager.
    mes_ini = mes.replace(day=1)
    mes_fin = mes_ini + relativedelta(months=1, days=-1)
    Q1 = models.Q(linea__fecha__isnull=False, linea__fecha__gte=mes_ini, linea__fecha__lte=mes_fin)
    Q2 = models.Q(linea__fecha__isnull=True, linea__asiento__fecha__gte=mes_ini, linea__asiento__fecha__lte=mes_fin)
    return Q1 | Q2


class LineaList(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        # la busqueda por fecha es lo que ha generado usar objetos Q
        query = models.Q(cuenta__espacio__site=self.site)

        # Esto es para poner las cosas que nos piden que busquen
        self.filters = {}

        # busqueda por cuenta
        cuenta = self.request.GET.get('cuenta')
        if cuenta:
            query &= models.Q(cuenta__nombre=cuenta)
            self.filters['cuenta'] = cuenta

        # busqueda por usuario
        usuario = self.request.GET.get('usuario')
        if usuario:
            query &= models.Q(miembro__user__username=usuario)
            self.filters['usuario'] = usuario

        # busqueda por mensualidad mm/yyyy
        mensualidad = self.request.GET.get('mensualidad', '')
        try:
            mensualidad = datetime.datetime.strptime(mensualidad, "%m/%Y").date()
        except ValueError:
            mensualidad = None
        if mensualidad:
            query &= objeto_q_linea_por_mes(mensualidad)
            self.filters['mensualidad'] = mensualidad

        # lets go
        return super(LineaList, self).get_queryset().filter(query).order_by('asiento__fecha', 'fecha')

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


class Ledger(SiteMixin, AdminOnly, ListView):
    model = Asiento
    template_name = "contabilidad/ledger.txt"
    content_type = "text/plain"


class ResumenPorMeses(SiteMixin, MemberOnly, TemplateView):
    template_name = "contabilidad/resumen_por_meses.html"

    def get_context_data(self, **kwargs):
        context = super(ResumenPorMeses, self).get_context_data(**kwargs)
        cuentas_qs = Cuenta.objects.filter(ver_miembros=True, espacio=self.espacio)
        cuentas = list(cuentas_qs)
        cuentas_dict = {cuenta.pk: i for i, cuenta in enumerate(cuentas)}
        columnas = [cuenta.nombre for cuenta in cuentas]

        fechas = Asiento.objects.all().aggregate(models.Min('fecha'), models.Max('fecha'))
        fecha = fechas['fecha__min'].replace(day=1)
        fecha_max = fechas['fecha__max'].replace(day=1)

        sumas = collections.OrderedDict()
        while fecha <= fecha_max:
            sumas[fecha] = [[0.0, c] for c in cuentas]
            cuentas_por_mes = cuentas_qs.filter(objeto_q_cuenta_por_mes(fecha)).annotate(models.Sum('linea__cantidad'))
            for c in cuentas_por_mes:
                index = cuentas_dict[c.pk]
                sumas[fecha][index][0] += c.linea__cantidad__sum if c.signo == "+" else -c.linea__cantidad__sum
            fecha += relativedelta(months=1)
        context['columnas'] = columnas
        context['sumas'] = sumas
        return context
