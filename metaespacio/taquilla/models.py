from django.conf import settings
from django.db import models

# Create your models here.


class Taquillero(models.Model):
    name = models.CharField(max_length=20)
    rows = models.IntegerField()
    cols = models.IntegerField()

    def __unicode__(self):
        return u"{} ({}x{})".format(self.name, self.row, self.col)


class Taquilla(models.Model):
    taquillero = models.ForeignKey(Taquillero)
    row = models.IntegerField()
    col = models.IntegerField()

    def __unicode__(self):
        return u"{} {}".format(self.row, self.col)


class AbonoTaquilla(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    taquilla = models.ForeignKey(Taquilla)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return u"{} {}".format(self.owner, self.taquilla)
