# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Espacio(models.Model):
    site = models.ForeignKey(Site)
    nombre = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    miembros = models.ManyToManyField(User, through='Miembro')
    logo = models.ImageField(upload_to="logos")

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

    def __unicode__(self):
        return "{}".format(self.nombre)


class Miembro(models.Model):
    espacio = models.ForeignKey(Espacio)
    user = models.ForeignKey(User)
    fecha_alta = models.DateField(auto_now=True)
    es_socio = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}@{}".format(self.user, self.espacio.slug)
