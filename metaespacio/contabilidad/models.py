from __future__ import unicode_literals
from django.db import models


class Cuenta(models.Model):
    nombre = models.CharField(max_length=255)
    espacio = models.ForeignKey('espacios.Espacio')
    ver_miembros = models.BooleanField(default=True)
    signo = models.CharField(max_length=1, choices=(('+', '+'), ('-', '-')), default='+')

    @property
    def signo_real(self):
        return 1 if self.signo == "+" else -1

    def __unicode__(self):
        return "{} ({})".format(self.nombre, self.signo)

    def suma(self):
        return self.linea_set.aggregate(models.Sum('cantidad'))['cantidad__sum']

    class Meta:
        ordering = ('espacio', 'nombre')
        unique_together = ('espacio', 'nombre')

    def nombre_sin_prefijo(self, prefijo):
        x = self.nombre[:]
        if x.startswith(prefijo):
            x = x[len(prefijo):]
            if x.startswith(":"):
                x = x[1:]
        return x

    def primer_nombre(self, prefijo=None):
        return self.nombre_sin_prefijo(prefijo).split(":")[0]

    def ultimo_nombre(self, prefijo=None):
        return self.nombre_sin_prefijo(prefijo).split(":")[-1]

    def subnombre(self, prefijo=None):
        if self.nombre.starswith(prefijo):
            x = x[len(prefijo):]
            if x.startswith(":"):
                x = x[1:]
        return x.split(":")[-1]


class Asiento(models.Model):
    espacio = models.ForeignKey('espacios.Espacio')
    concepto = models.CharField(max_length=255)
    fecha = models.DateField()

    def __unicode__(self):
        return "{} {}".format(self.concepto, self.fecha)

    def diferencia(self, prefijo=None):
        qs = self.linea_set.all()
        if prefijo:
            qs = qs.filter(cuenta__nombre__startswith=prefijo)
        return qs.aggregate(models.Sum('cantidad'))['cantidad__sum']


class Linea(models.Model):
    asiento = models.ForeignKey(Asiento)
    cuenta = models.ForeignKey(Cuenta)
    cantidad = models.FloatField()
    miembro = models.ForeignKey('espacios.Miembro', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    @property
    def cantidad_user(self):
        return self.cantidad if self.cuenta.signo == "+" else -self.cantidad

    def fecha_str(self):
        return self.fecha if self.fecha else self.asiento.fecha

    def cuenta_str(self):
        if self.fecha:
            return "{}:{}:{:02d}".format(self.cuenta.nombre, self.fecha.year, self.fecha.month)
        elif self.miembro:
            return "{}:{}".format(self.cuenta.nombre, self.miembro.user.username)
        else:
            return "{}".format(self.cuenta.nombre)

    def __unicode__(self):
        if self.miembro:
            cuenta = "{} de {}".format(self.cuenta, self.miembro.user)
        else:
            cuenta = unicode(self.cuenta)
        return "{:+.2f} ({})".format(self.cantidad, cuenta)

    class Meta:
        ordering = ('asiento', '-cantidad', '-fecha')
