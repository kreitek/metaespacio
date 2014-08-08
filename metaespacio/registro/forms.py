# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email',
                  'dni', 'direccion', 'telefono']

