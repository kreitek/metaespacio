# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from espacios.models import Espacio


class Pagina(models.Model):
    espacio = models.ForeignKey(Espacio)
    orden = models.IntegerField(default=0)
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        unique_together = (('espacio', 'slug'), )
        ordering = ('espacio', 'orden')
