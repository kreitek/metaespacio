from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Taquillero(models.Model):
    name = models.CharField(max_lenght=20)
    rows = models.IntegerField()
    cols = models.IntegerField()

    def __unicode__(self):
        return self.name


class Taquilla(models.Model):
    taquillero = models.ForeignKey(Taquillero)
    row = models.IntegerField()
    col = models.IntegerField()

    def __unicode__(self):
        return "1"


class AbonoTaquilla(models.Model):
    owner = models.ForeignKey(get_user_model()
    taquilla = models.ForeignKey(Taquilla)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return u"{} {}".format(self.owner, self.taquilla)