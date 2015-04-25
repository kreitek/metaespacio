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

    def __unicode__(self):
        return "{}".format(self.nombre)


class Miembro(models.Model):
    espacio = models.ForeignKey(Espacio)
    user = models.ForeignKey(User)
    fecha_alta = models.DateField(auto_now=True)

    def __unicode__(self):
        return "{}@{}".format(self.user, self.espacio.slug)
