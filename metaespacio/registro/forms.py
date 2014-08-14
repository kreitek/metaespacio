# -*- coding: utf-8 -*-

from django import forms
from localflavor.es.forms import ESIdentityCardNumberField
from captcha.fields import CaptchaField
from .models import Usuario
from django.contrib.auth.models import User
import string


def cuenta_upper_lower_digits_other(cadena):
    upper = lower = digits = other = 0
    for ch in cadena:
        if ch in string.lowercase:
            lower += 1
        elif ch in string.uppercase:
            upper += 1
        elif ch in string.digits:
            digits += 1
        else:
            other += 1
    return upper, lower, digits, other


class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label=u"Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label=u"Contraseña", widget=forms.PasswordInput)
    captcha = CaptchaField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).count() > 0:
            raise forms.ValidationError(u"El nombre de usuario está en uso")
        return username

    def clean_password1(self):
        passwd = self.cleaned_data['password1']
        upper, lower, digits, other = cuenta_upper_lower_digits_other(passwd)
        required = []
        if len(passwd) < 8:
            required.append(u"8 caracteres")
        if upper == 0:
            required.append(u"una mayúscula")
        if lower == 0:
            required.append(u"una minúscula")
        if digits == 0:
            required.append(u"un número")
        if len(required) > 0:
            msg = u"Requerido: {}".format(", ".join(required))
            raise forms.ValidationError(msg)
        return passwd

    def clean(self):
        cleaned_data = super(UsuarioForm, self).clean()
        dni = cleaned_data.get("dni")
        try:
            ESIdentityCardNumberField().clean(dni)
        except forms.ValidationError:
            raise forms.ValidationError("El número identificador no es válido")
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas deben coincidir")
        return cleaned_data

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email',
                  'dni', 'direccion', 'telefono']
