from __future__ import unicode_literals
from django.db import models


class Cuenta(models.Model):
    nombre = models.CharField(max_length=255)
    espacio = models.ForeignKey('espacios.Espacio')
    ver_miembros = models.BooleanField(default=True)
    signo = models.CharField(max_length=1, choices=(('+', '+'), ('-', '-')), default='+')

    def __unicode__(self):
        return "{} ({})".format(self.nombre, self.signo)

    def suma(self):
        return self.linea_set.aggregate(models.Sum('cantidad'))['cantidad__sum']

    class Meta:
        ordering = ('espacio', 'nombre')
        unique_together = ('espacio', 'nombre')


class Asiento(models.Model):
    espacio = models.ForeignKey('espacios.Espacio')
    concepto = models.CharField(max_length=255)
    fecha = models.DateField()

    def __unicode__(self):
        return "{} {}".format(self.concepto, self.fecha)


class Linea(models.Model):
    asiento = models.ForeignKey(Asiento)
    cuenta = models.ForeignKey(Cuenta)
    cantidad = models.FloatField()
    miembro = models.ForeignKey('espacios.Miembro', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    def __unicode__(self):
        if self.miembro:
            cuenta = "{} de {}".format(self.cuenta, self.miembro.user)
        else:
            cuenta = unicode(self.cuenta)
        return "{:+.2f} ({})".format(self.cantidad, cuenta)

    class Meta:
        ordering = ('asiento', '-cantidad')
