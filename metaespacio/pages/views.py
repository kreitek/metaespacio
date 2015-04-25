# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from .models import Pagina
from espacios.views import FilterEspacioSiteMixin


class PaginaView(FilterEspacioSiteMixin, DetailView):
     model = Pagina
