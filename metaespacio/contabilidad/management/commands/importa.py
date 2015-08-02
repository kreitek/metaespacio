# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from contabilidad.models import Cuenta, Asiento, Linea
from espacios.models import Espacio
from cuotas.models import FormaPago, Pago


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('cuenta_contado', type=int)
        # parser.add_argument('cuenta_mensualidad', type=int)
        pass

    def handle(self, *args, **options):
        1/0

        espacio = Espacio.objects.get(nombre__startswith="Andén")
        self.stdout.write("# Usando espacio: {}".format(espacio))

        self.stdout.write("Borradas todas las cuentas previas")
        Cuenta.objects.all().delete()

        self.stdout.write("Creando cuentas")
        cuenta_contado = Cuenta.objects.create(nombre="Activo:Contado", espacio=espacio)
        cuenta_bancaria = Cuenta.objects.create(nombre="Activo:Triodos", espacio=espacio)
        cuenta_mensualidad = Cuenta.objects.create(nombre="Ingresos:Cuotas", espacio=espacio, signo='-')
        Cuenta.objects.create(nombre="Gastos:AguaLuz", espacio=espacio, signo='+')
        Cuenta.objects.create(nombre="Gastos:Internet", espacio=espacio, signo='+')
        Cuenta.objects.create(nombre="Gastos:Cachibaches", espacio=espacio, signo='+')
        Cuenta.objects.create(nombre="ValorDonacion", espacio=espacio, signo='-')
        Cuenta.objects.create(nombre="Patrimonio:Material", espacio=espacio, signo='+')
        cuenta_origen = Cuenta.objects.create(nombre="?? Ingreso ??", espacio=espacio, signo='-')
        cuenta_destino = Cuenta.objects.create(nombre="?? Gasto ??", espacio=espacio, signo='+')

        forma_contado = FormaPago.objects.get(nombre='En Metalico (cuotas)')
        forma_bancaria = FormaPago.objects.get(nombre='Cargo a cuenta')
        forma_bancaria2 = FormaPago.objects.get(nombre='Por transferencia')

        self.stdout.write("Borrados todos los asientos previos")
        Asiento.objects.all().delete()

        for pago in Pago.objects.order_by('id'):
            if pago.forma_pago == forma_contado:
                cuenta1 = cuenta_contado
                cuenta2 = cuenta_mensualidad
            elif pago.forma_pago in [forma_bancaria, forma_bancaria2]:
                cuenta1 = cuenta_bancaria
                cuenta2 = cuenta_mensualidad
            else:
                cuenta1 = cuenta_origen
                cuenta2 = cuenta_destino

            asiento = Asiento.objects.create(fecha=pago.fecha, concepto=pago.description, espacio=espacio)
            Linea.objects.create(asiento=asiento, cantidad=pago.cantidad, cuenta=cuenta1)
            for mensualidad in pago.mensualidad_set.all():
                fecha = mensualidad.fecha.replace(day=1)
                Linea.objects.create(asiento=asiento, cantidad=-mensualidad.cantidad, miembro=mensualidad.miembro, cuenta=cuenta2, fecha=fecha)
            self.stdout.write('Pago {} crea asiento {}: {}'.format(pago.pk, asiento.pk, asiento))
