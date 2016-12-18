from django.views.generic import ListView, TemplateView
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from dateutil.relativedelta import relativedelta
import collections
import datetime
import urllib
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


def objeto_q_linea_futura(mes):
    # Tenemos el problema de que las fechas en las lineas son opcionales y las fechas
    # en los asientos obligatorios. Esto es para hacer busquedas por fecha sobre
    # asientos. FIXME esto se puede meter como un manager en los modelos y queda
    # mejor.
    mes_ini = mes.replace(day=1) + relativedelta(months=1)
    Q1 = models.Q(fecha__isnull=False, fecha__gte=mes_ini)
    Q2 = models.Q(fecha__isnull=True, asiento__fecha__gte=mes_ini)
    return Q1 | Q2


def objeto_q_cuenta_por_mes(mes):
    # Es igual que el anterior agregando linea__ para hacer busquedas por fecha
    # sobre cuentas. FIXME idem meter en un manager.
    mes_ini = mes.replace(day=1)
    mes_fin = mes_ini + relativedelta(months=1, days=-1)
    Q1 = models.Q(linea__fecha__isnull=False, linea__fecha__gte=mes_ini, linea__fecha__lte=mes_fin)
    Q2 = models.Q(linea__fecha__isnull=True, linea__asiento__fecha__gte=mes_ini, linea__asiento__fecha__lte=mes_fin)
    return Q1 | Q2


def objeto_q_cuenta_futura(mes):
    # Es igual que el anterior agregando linea__ para hacer busquedas por fecha
    # sobre cuentas. FIXME idem meter en un manager.
    mes_ini = mes.replace(day=1) + relativedelta(months=1)
    Q1 = models.Q(linea__fecha__isnull=False, linea__fecha__gte=mes_ini)
    Q2 = models.Q(linea__fecha__isnull=True, linea__asiento__fecha__gte=mes_ini)
    return Q1 | Q2


class LineaList(SiteMixin, MemberOnly, ListView):
    model = Linea
    paginate_by = 20

    def get_queryset(self):
        # la busqueda por fecha es lo que ha generado usar objetos Q
        query = models.Q(cuenta__espacio__site=self.site)

        # Esto es para poner las cosas que nos piden que busquen
        self.filtros = {}

        # busqueda por cuenta
        cuenta = self.request.GET.get('cuenta')
        if cuenta:
            query &= models.Q(cuenta__nombre__startswith=cuenta)
            self.filtros['cuenta'] = cuenta

        # busqueda por usuario
        usuario = self.request.GET.get('usuario')
        if usuario:
            query &= models.Q(miembro__user__username=usuario)
            self.filtros['usuario'] = usuario

        # busqueda por mensualidad mm/yyyy
        mensualidad = self.request.GET.get('mensualidad', '')
        if mensualidad == 'prevision':
            query &= objeto_q_linea_futura(datetime.datetime.now().date())
            self.filtros['mensualidad'] = 'prevision'
        else:
            try:
                mensualidad = datetime.datetime.strptime(mensualidad, "%m/%Y").date()
            except ValueError:
                mensualidad = None
            if mensualidad:
                query &= objeto_q_linea_por_mes(mensualidad)
                self.filtros['mensualidad'] = mensualidad.strftime("%m/%Y")

        # lets go
        return super(LineaList, self).get_queryset().filter(query).order_by('-asiento__fecha', '-fecha')

    def get_context_data(self, **kwargs):
        context = super(LineaList, self).get_context_data(**kwargs)
        context['filtros'] = self.filtros
        context['filtros_str'] = urllib.urlencode({k: v.encode('utf-8') for k, v in self.filtros.items()})
        return context


class LineasUsuario(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        kwargs = {"miembro__espacio__site": self.site}
        username = self.kwargs.get('username')
        if username:
            url_user = get_object_or_404(User, username=username)
            kwargs["miembro__user"] = url_user
        return super(LineasUsuario, self).get_queryset().filter(**kwargs).order_by('-asiento__fecha', '-fecha')

    def get_context_data(self, **kwargs):
        context = super(LineasUsuario, self).get_context_data(**kwargs)
        context['titulo'] = self.kwargs.get('username')
        return context


class LineasCuenta(SiteMixin, MemberOnly, ListView):
    model = Linea

    def get_queryset(self):
        self.cuenta = get_object_or_404(Cuenta, espacio=self.espacio, pk=self.kwargs['pk'])
        return super(LineasCuenta, self).get_queryset().filter(cuenta=self.cuenta).order_by('-fecha')

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

        # empezamos con las cuentas del espacio para todos los publicos
        cuentas_qs = Cuenta.objects.filter(ver_miembros=True, espacio=self.espacio)

        # y filtramos por startwith del nombre de las cuentas si nos lo pasan
        prefijo = self.request.GET.get('cuentas', '')
        if prefijo:
            cuentas_qs = cuentas_qs.filter(nombre__startswith=prefijo)

        # Siendo la cuenta "Noseque:Cosa" y el prefijo "Noseque:", el primer_nombre es "Cosa"
        pk_nom_subnom = [
            (cuenta.pk, cuenta.nombre, cuenta.primer_nombre(prefijo))
            for i, cuenta in enumerate(cuentas_qs)
            ]
        # Nuestras columnas van a ser todos los subnombres diferentes
        columnas = sorted(set([subnom for pk, nom, subnom in pk_nom_subnom]))
        # Y este es el array de transformacion de pk a que numero de columna le toca
        pk_dict = {pk: columnas.index(subnom) for pk, nom, subnom in pk_nom_subnom}

        # Nos quedamos con el minimo-maximo de los asientos en BD
        fechas = Asiento.objects.all().aggregate(models.Min('fecha'), models.Max('fecha'))
        fecha = fechas['fecha__min'].replace(day=1)
        fecha_max = fechas['fecha__max'].replace(day=1)
        fecha_hoy = datetime.datetime.now().date().replace(day=1)

        # El diccionario estara ordenado crecientemente. Recordar el orden.
        sumas = collections.OrderedDict()
        total = collections.OrderedDict(zip(columnas, [0.0]*len(columnas)))
        while fecha <= fecha_max:
            sumas[fecha] = [[0.0, c] for c in columnas]
            cuentas_por_mes = cuentas_qs  \
                .filter(objeto_q_cuenta_por_mes(fecha))  \
                .annotate(models.Sum('linea__cantidad'))
            for c in cuentas_por_mes:
                index = pk_dict[c.pk]
                acc = c.linea__cantidad__sum if c.signo == "+" else -c.linea__cantidad__sum
                sumas[fecha][index][0] += acc
                total[c.primer_nombre(prefijo)] += acc
            fecha += relativedelta(months=1)

        # El diccionario estara ordenado crecientemente. Recordar el orden.
        total_prev = collections.OrderedDict(zip(columnas, [0.0]*len(columnas)))
        sumas_prev = [[0.0, c] for c in columnas]
        cuentas_futuras = cuentas_qs  \
            .filter(objeto_q_cuenta_futura(fecha_hoy))  \
            .annotate(models.Sum('linea__cantidad'))
        for c in cuentas_futuras:
            index = pk_dict[c.pk]
            acc = c.linea__cantidad__sum if c.signo == "+" else -c.linea__cantidad__sum
            sumas_prev[index][0] += acc
            total[c.primer_nombre(prefijo)] += acc


        context['prefijo'] = prefijo if prefijo else ""
        context['columnas'] = columnas
        context['sumas'] = sumas
        context['prevision'] = sumas_prev
        context['total'] = total
        context['cuentas_por_mes'] = cuentas_por_mes
        return context


class Oficial(SiteMixin, MemberOnly, TemplateView):
    template_name = "contabilidad/oficial.html"

    def get_context_data(self, **kwargs):
        context = super(Oficial, self).get_context_data(**kwargs)

        # empezamos con las cuentas del espacio para todos los publicos
        cuentas_qs = Cuenta.objects.filter(ver_miembros=True, espacio=self.espacio)

        # y filtramos por startwith del nombre de las cuentas si nos lo pasan
        prefijo = self.request.GET.get('cuentas', 'Oficial')
        cuentas_qs = cuentas_qs.filter(nombre__startswith=prefijo)

        # Siendo la cuenta "Noseque:Cosa:Tal" y el prefijo "Noseque:", el ultimo_nombre es "Tal"
        pk_nom_subnom = [
            (cuenta.pk, cuenta.nombre, cuenta.nombre_sin_prefijo(prefijo))
            for i, cuenta in enumerate(cuentas_qs)
            ]
        # Nuestras columnas van a ser todos los subnombres diferentes
        columnas = sorted(set([subnom for pk, nom, subnom in pk_nom_subnom]))
        # Y este es el array de transformacion de pk a que numero de columna le toca
        pk_dict = {pk: columnas.index(subnom) for pk, nom, subnom in pk_nom_subnom}

        # El diccionario estara ordenado crecientemente. Recordar el orden.
        year = self.kwargs.get('year')
        asientos_qs = Asiento.objects.all()
        if year:
            asientos_qs = asientos_qs.filter(fecha__year=year)
        asientos_qs = asientos_qs.filter(linea__cuenta__in=cuentas_qs).order_by('fecha').distinct()

        asientos = []
        total = [0.0 for c in columnas]
        for a in asientos_qs:
            for l in a.linea_set.filter(cuenta__in=cuentas_qs):
                index = pk_dict[l.cuenta.pk]
                total[index] += l.cantidad
            asientos.append([a, total[:]])

        context['columnas'] = columnas
        context['asientos'] = asientos
        return context
