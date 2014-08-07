# -*- coding: utf-8 -*-

from django import forms
from .models import EspacioUser

class EspacioUserForm(forms.ModelForm):
    class Meta:
        model = EspacioUser
        fields = ['first_name', 'last_name', 'username', 'email',
                  'dni', 'direccion', 'telefono']
