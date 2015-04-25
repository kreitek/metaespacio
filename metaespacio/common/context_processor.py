# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from espacios.models import Espacio


def site(request):
    site = get_current_site(request)
    espacio = site.espacio_set.first()
    espacios = Espacio.objects.all()
    return {'site': site, 'espacio': espacio, 'espacios': espacios}
