# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import os


def _upload_to(self, filename):
    basename, extension = os.path.splitext(filename)
    return "contabilidad/{}/{:02d}/{}".format(self.fecha_factura.year, self.fecha_factura.month, filename)


class Validacion(models.Model):
    espacio = models.ForeignKey('espacios.Espacio', related_name="validaciones")
    nombre = models.CharField(max_length=255)
    es_donacion = models.BooleanField(help_text="No se espera contrapartida")
    es_metalico = models.BooleanField()
    es_oficial = models.BooleanField(help_text="Tiene factura o fue por el banco")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "validación"
        verbose_name_plural = "validaciones"
        ordering = ('espacio', 'nombre')


class Categoria(models.Model):
    espacio = models.ForeignKey('espacios.Espacio', related_name="categorias")
    nombre = models.CharField(max_length=255)
    ayuda = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        if self.ayuda:
            return "{} ({})".format(self.nombre, self.ayuda)
        else:
            return "{}".format(self.nombre)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ('espacio', 'nombre')


class Registro(models.Model):
    espacio = models.ForeignKey('espacios.Espacio', related_name="registros")
    miembro = models.ForeignKey('espacios.Miembro', blank=True, null=True)
    fecha_formulario = models.DateTimeField(auto_now_add=True)

    concepto = models.CharField(max_length=255)
    fecha_factura = models.DateField(verbose_name="fecha de factura")
    es_donado = models.BooleanField(help_text="Marca la casilla si no quieres dinero por ello")
    categoria = models.ForeignKey(Categoria, verbose_name="categoría")
    importe = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.FileField(upload_to=_upload_to, blank=True, null=True)
    factura = models.FileField(upload_to=_upload_to, blank=True, null=True)

    validacion = models.ForeignKey(Validacion, verbose_name="validación", blank=True, null=True)
    fecha_pago = models.DateField(verbose_name="fecha de pago", blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{} {}".format(self.fecha_factura, self.concepto)

    class Meta:
        ordering = ('espacio', 'fecha_factura')
