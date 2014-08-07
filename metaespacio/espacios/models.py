from django.db import models
from registro.models import Usuario


class Espacio(models.Model):
    nombre = models.CharField(max_length=60)
    miembros = models.ManyToManyField(Usuario, through='MiembroEspacio')

    def __unicode__(self):
        return self.nombre


class MiembroEspacio(models.Model):
    espacio = models.ForeignKey(Espacio)
    usuario = models.ForeignKey(Usuario)
    fecha_alta = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}@{} ({})".format(self.usuario, self.espacio, self.fecha_alta.date())
