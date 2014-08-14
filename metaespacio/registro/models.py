# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Usuario(User):
    dni = models.CharField(max_length=9)
    direccion = models.TextField(help_text=u"Dirección postal completa, puede tener varias líneas")
    telefono = models.CharField(max_length=9)

    def get_absolute_url(self):
        return reverse("detail_user", kwargs={'pk': self.pk})
