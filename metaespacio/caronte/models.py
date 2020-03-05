# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from espacios.models import Espacio


class Lector(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    espacio = models.ForeignKey('espacios.Espacio')
    last_uptime = models.DateTimeField(blank=True, null=True)

    def uptime(self, now=None):
        if not now:
            now = timezone.now()
        self.last_uptime = now
        self.save()

    def __unicode__(self):
        return "{} ({})".format(self.nombre, self.slug)

    class Meta:
        verbose_name_plural = "lectores"


class Autorizacion(models.Model):
    user = models.ForeignKey(User)
    codigo = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return "{} ({})".format(self.codigo, self.user)

    class Meta:
        verbose_name = 'autorización'
        verbose_name_plural = 'autorizaciones'


class EntradaSalida(models.Model):
    user = models.ForeignKey(User)
    espacio = models.ForeignKey(Espacio)
    entrada = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(blank=True, null=True)

    def dentro(self):
        return not self.salida

    def sale(self, now=None):
        if not now:
            now = timezone.now()
        if self.salida:
            print("error, ya salio")
        else:
            self.salida = now
            self.save()

    def __unicode__(self):
        return "{}@{} ({}-{})".format(self.user, self.espacio, self.entrada, self.salida or "X")

    class Meta:
        ordering = ['-entrada']
        verbose_name = 'entrada y salida'
        verbose_name_plural = 'entradas y salidas'

