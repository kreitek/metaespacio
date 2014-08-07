# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User

class Usuario(User):
    dni = models.CharField(max_length=9)
    direccion = models.TextField(help_text=u"Dirección postal completa, puede tener varias líneas")
    telefono = models.CharField(max_length=9)
