# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from espacios.models import Espacio, Miembro


class Taquillero(models.Model):
    espacio = models.ForeignKey(Espacio)
    name = models.CharField(max_length=20)
    rows = models.IntegerField()
    cols = models.IntegerField()

    def __unicode__(self):
        return "{}@{}".format(self.name, self.espacio.slug)

    class Meta:
        unique_together = (('espacio', 'name'), )


class Taquilla(models.Model):
    taquillero = models.ForeignKey(Taquillero)
    row = models.IntegerField()
    col = models.IntegerField()

    def __unicode__(self):
        return "({},{}) en {}".format(self.row, self.col, self.taquillero)

    class Meta:
        unique_together = (('taquillero', 'row', 'col'), )


class Abono(models.Model):
    miembro = models.ForeignKey(Miembro)
    taquilla = models.ForeignKey(Taquilla)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return "{} {}".format(self.miembro, self.taquilla)
