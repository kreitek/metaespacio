# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    ext = filename.split(".")[-1]
    return "avatares/{}.{}".format(instance.user.username, ext)


class DatosPersonales(models.Model):
    user = models.OneToOneField(User)
    dni = models.CharField(max_length=9)
    direccion = models.TextField(help_text="Dirección postal completa, puede tener varias líneas")
    telefono = models.CharField(max_length=9)
    avatar = models.ImageField(upload_to=upload_to)

    def __unicode__(self):
        return "{} ({})".format(self.user, self.dni)

    class Meta:
        verbose_name = "dato personal"
        verbose_name_plural = "datos personales"


class Mac(models.Model):
    user = models.ForeignKey(User)
    mac = models.CharField(max_length=20)

    def __unicode__(self):
        return "{} ({})".format(self.mac, self.user)
