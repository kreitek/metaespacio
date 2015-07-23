# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from .models import Pagina
from espacios.views import FilterEspacioSiteMixin
from django.contrib import messages


class PaginaView(FilterEspacioSiteMixin, DetailView):
    model = Pagina

    def get_object(self):
        _object = super(PaginaView, self).get_object()
        if _object.privado and not self.miembro is None:
            return _object
        else:
            # FIXME: El mensaje de error afecta tambien a la renderizacion
            #        del menu, por lo que para usuarios no autenticados
            #        ahora siempre se mostraría si hay paginas privadas
            #messages.error(self.request, 'Necesita autorización para acceder')
            return self.get_queryset().first()


class PaginaIndex(PaginaView):

    def get_object(self):
        return self.get_queryset().first()
