# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from espacios.models import Espacio, Miembro
import datetime


class FormaPago(models.Model):
    "Efectivo, Cuenta corriente, Stripe?, Otras"
    espacio = models.ForeignKey(Espacio)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    # for fp in anden.formapago_set.all():
    #     print fp.nombre, sum(fp.pago_set.values_list("cantidad"))


class CuotaPeriodica(models.Model):
    "Cantidad mensual a aportar por miembro"
    forma_pago = models.ForeignKey(FormaPago)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)
    cantidad = models.FloatField()


class Pago(models.Model):
    pagador = models.ForeignKey(Miembro)
    fecha_pago = models.DateField()
    cantidad = models.FloatField()
    forma_pago = models.ForeignKey(FormaPago)
    description = models.CharField(max_length=255, blank=True, null=True)

    @property
    def fecha_inicio(self):
        return self.fecha_efecto or self.fecha_pago

    @property
    def dias(self):
        # FIXME arreglar esto y que sea mensual++
        # (buscar libreria de timedeltas avanzados)
        return int(self.cantidad * self.forma_pago.cantidad / 30.0)

    @property
    def fecha_final(self):
        return self.fecha_inicio + datetime.timedelta(days=self.dias)

    # class Meta:
    #     ordering = ('miembro', 'fecha_pago')


class Mensualidad(models.Model):
    pago = models.ForeignKey(Pago)
    miembro = models.ForeignKey(Miembro)
    fecha_efecto = models.DateField(blank=True, null=True)
    cantidad = models.FloatField()

    @property
    def fecha_inicio(self):
        return self.fecha_efecto or self.fecha_pago
