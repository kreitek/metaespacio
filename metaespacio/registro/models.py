# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class DatosPersonales(models.Model):
    user = models.OneToOneField(User)
    dni = models.CharField(max_length=9)
    direccion = models.TextField(help_text="Dirección postal completa, puede tener varias líneas")
    telefono = models.CharField(max_length=9)
    avatar = models.ImageField(upload_to="avatares")

    def __unicode__(self):
        return "{} ({})".format(self.user, self.dni)


class Mac(models.Model):
    user = models.ForeignKey(User)
    mac = models.CharField(max_length=20)

    def __unicode__(self):
        return "{} ({})".format(self.mac, self.user)
