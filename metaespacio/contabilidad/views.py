from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from espacios.views import SiteMixin, MemberOnly
from .models import Linea, Cuenta


class LineaList(ListView):
    model = Linea


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
