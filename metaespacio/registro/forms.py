from django import forms
# from localflavor.es.forms import ESIdentityCardNumberField
from django.contrib.auth.models import User
import string
import re


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


PREGUNTAS_RESPUESTAS = [
    # FIXME estaria bien que el formulario escogiera una pregunta aleatoria
    # de estas, pero de momento no ponemos sino
    ("Duemilanove, uno, yun, leonardo, ... ¿que son?", "arduino"),
]


class UserForm(forms.ModelForm):
    PASSWORD_HELP_TEXT = "Contraseña de un mínimo de 8 caracteres con una mayúscula, una minúscula y un número"
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text=PASSWORD_HELP_TEXT)
    password2 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, help_text=PASSWORD_HELP_TEXT)
    captcha = forms.CharField(label="Pregunta secreta", help_text=PREGUNTAS_RESPUESTAS[0][0])

    def clean_captcha(self):
        respuesta = self.cleaned_data['captcha'].lower().strip()
        if respuesta != PREGUNTAS_RESPUESTAS[0][1]:
            raise forms.ValidationError("Lo siento, pero para darte de alta tienes que responder "
                                        "correctamente a la pregunta secreta")
        return respuesta

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).count() > 0:
            raise forms.ValidationError("El nombre de usuario está en uso")
        # BUG: El mensaje de ayuda del username entra en contradicción con la siguiente validación
        if re.match(r"^([a-zA-Z0-9_])+$", username) is None:
            raise forms.ValidationError("El nombre de usuario solo debe contener letras o cifras o _")
        return username

    def clean_password1(self):
        passwd = self.cleaned_data['password1']
        upper, lower, digits, other = cuenta_upper_lower_digits_other(passwd)
        required = []
        if len(passwd) < 8:
            required.append("8 caracteres")
        if upper == 0:
            required.append("una mayúscula")
        if lower == 0:
            required.append("una minúscula")
        if digits == 0:
            required.append("un número")
        if len(required) > 0:
            msg = "Requerido: {}".format(", ".join(required))
            raise forms.ValidationError(msg)
        return passwd

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        # dni = cleaned_data.get("dni")
        # try:
        #     ESIdentityCardNumberField().clean(dni)
        # except forms.ValidationError:
        #    raise forms.ValidationError("El número identificador (DNI) no es válido")
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas deben coincidir")
        return cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
