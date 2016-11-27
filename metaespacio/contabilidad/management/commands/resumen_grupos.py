# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from contabilidad.models import Asiento, Cuenta


class Command(BaseCommand):
    help = 'Resumen de lineas que se usan en los asientos'

    def handle(self, *args, **options):
        grupos = {}

        # buscamos las cuentas de cada asiento
        for asiento in Asiento.objects.all():
            cuentas = Cuenta.objects.filter(linea__asiento=asiento).distinct()
            # indexamos por algo unico
            key = unicode(sorted([cuenta.pk for cuenta in cuentas]))
            # el primer item de la lista es el listado de cuentas
            if key not in grupos:
                grupos[key] = [cuentas]
            # el resto de items son los asientos intervinientes
            grupos[key].append(asiento)

        # mostramos la cuenta de asientos implicados a cada grupo de cuentas relacionadas
        for items in grupos.values():
            cuentas = items.pop(0)
            resultado = [len(items)] + list(cuentas)
            msg = ",".join(unicode(x) for x in resultado)
            self.stdout.write(msg + "\n")
