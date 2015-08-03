import os.path
from django.db import models
from contabilidad.models import Asiento


def _upload_to(self, filename):
    basename, extension = os.path.splitext(filename)
    return "contabilidad/{}{}".format(self.asiento.pk, extension)


class AdjuntoAsiento(models.Model):
    asiento = models.ForeignKey(Asiento)
    fichero = models.FileField(upload_to=_upload_to)
