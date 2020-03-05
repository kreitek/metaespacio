# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils import timezone
from contabilidad.models import Cuenta


def logos_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    return "logos/{}.{}".format(instance.slug, ext)


def favicons_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    return "favicons/{}.{}".format(instance.slug, ext)

# esto es para que una migration vieja se calle (no usar)
upload_to = logos_upload_to


class Espacio(models.Model):
    site = models.ForeignKey(Site)
    nombre = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    miembros = models.ManyToManyField(User, through='Miembro')
    logo = models.ImageField(upload_to=logos_upload_to, blank=True, null=True)
    favicon = models.ImageField(upload_to=favicons_upload_to, blank=True, null=True, help_text="El formato debe ser PNG y tamaño 16x16 o 32x32")

    #contabilidad
    cuotas = models.ManyToManyField(Cuenta, related_name='cuenta_de')
    cuota_minima = models.FloatField(null=True)

    # enlaces redes sociales y otros
    facebook_fanpage = models.URLField(blank=True, null=True)
    facebook_group = models.URLField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)
    google_group = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    www = models.URLField(blank=True, null=True)
    blog = models.URLField(blank=True, null=True)
    google_site = models.URLField(blank=True, null=True)

    def esta_abierto(self, now=None):
        if not now:
            now = timezone.now()
        qs = self.entradasalida_set.filter(entrada__lt=now, salida__isnull=True)
        return qs.exists()

    def cierra(self, now=None):
        if not now:
            now = timezone.now()
        qs = self.entradasalida_set.filter(entrada__gt=now, salida__isnull=True)
        qs.update(salida=now)

    def __unicode__(self):
        return "{}".format(self.nombre)


class Miembro(models.Model):
    espacio = models.ForeignKey(Espacio)
    user = models.ForeignKey(User)
    fecha_alta = models.DateField(auto_now=True)
    es_socio = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}@{}".format(self.user, self.espacio.slug)
