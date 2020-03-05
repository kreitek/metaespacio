from django.db import models
from django.utils import timezone
from espacios.models import Espacio, Miembro


class Encuesta(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    pregunta = models.CharField(max_length=255)
    texto = models.TextField(blank=True)
    voto_anonimo = models.BooleanField()
    voto_multiple = models.BooleanField()
    voto_editable = models.BooleanField()

    @property
    def finalizada(self):
        return self.fecha_finalizacion and timezone.now() > self.fecha_finalizacion

    def opcion_count(self):
        return self.opcion_set.count()

    def voto_count(self):
        return Voto.objects.filter(opcion__encuesta=self).count()

    def miembro_count(self):
        return Miembro.objects.filter(voto__opcion__encuesta=self).order_by('pk').distinct().count()

    def __str__(self):
        return "{}".format(self.pregunta)


class Opcion(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    eleccion = models.CharField(max_length=255)
    texto = models.TextField(blank=True)

    def voto_count(self):
        return self.voto_set.count()

    def __str__(self):
        return "{}".format(self.eleccion)


class Voto(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} vota {}'.format(self.miembro, self.opcion)
