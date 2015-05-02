# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from espacios.models import Espacio, Miembro


class FormaPago(models.Model):
    "Efectivo, Cuenta corriente, Stripe?, Otras"
    espacio = models.ForeignKey(Espacio)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    porcentaje_comision = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "forma de pago"
        verbose_name_plural = "formas de pago"


class CuotaPeriodica(models.Model):
    "Cantidad mensual a aportar por miembro"
    espacio = models.ForeignKey(Espacio)
    cantidad = models.FloatField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "{} euros/mes [{}-{}]".format(
            self.cantidad,
            self.fecha_inicial.strftime("%m/%y"),
            self.fecha_final.strftime("%m/%y") if self.fecha_final else "-")

    class Meta:
        verbose_name = "cuota periódica"
        verbose_name_plural = "cuotas periódicas"


class Pago(models.Model):
    pagador = models.ForeignKey(Miembro)
    fecha = models.DateField()
    cantidad = models.FloatField()
    forma_pago = models.ForeignKey(FormaPago)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "{} pagó {:.2f} € el dia {} por {}".format(
            self.pagador,
            self.cantidad,
            self.fecha,
            self.forma_pago)

    class Meta:
        ordering = ('fecha', )


class Mensualidad(models.Model):
    pago = models.ForeignKey(Pago)
    miembro = models.ForeignKey(Miembro)
    fecha_efecto = models.DateField(blank=True, null=True)
    cantidad = models.FloatField()

    @property
    def fecha_inicio(self):
        return self.fecha_efecto or self.fecha_pago

    class Meta:
        ordering = ('fecha_efecto', )
        verbose_name = "mensualidad"
        verbose_name_plural = "mensualidades"
