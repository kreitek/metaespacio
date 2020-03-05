from django.db import models
from espacios.models import Espacio, Miembro


class Taquillero(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    rows = models.IntegerField()
    cols = models.IntegerField()

    def __str__(self):
        return "{}@{}".format(self.name, self.espacio.slug)

    class Meta:
        unique_together = (('espacio', 'name'), )


class Taquilla(models.Model):
    taquillero = models.ForeignKey(Taquillero, on_delete=models.CASCADE)
    row = models.IntegerField()
    col = models.IntegerField()

    def __str__(self):
        return "({},{}) en {}".format(self.row, self.col, self.taquillero)

    class Meta:
        unique_together = (('taquillero', 'row', 'col'), )


class Abono(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    taquilla = models.ForeignKey(Taquilla, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.miembro, self.taquilla)
