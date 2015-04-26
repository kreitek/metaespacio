# -*- coding: utf-8 -*-
from django import forms


class EncuestaFormMulti(forms.Form):
    def __init__(self, encuesta, *args, **kwargs):
        super(EncuestaFormMulti, self).__init__(*args, **kwargs)
        for opcion in encuesta.opcion_set.all():
            key = "opcion_{}".format(opcion.pk)
            self.fields[key] = forms.BooleanField(label=opcion.eleccion, required=False)


class EncuestaFormChoice(forms.Form):
    answer = forms.ChoiceField(required=False)

    def __init__(self, encuesta, *args, **kwargs):
        super(EncuestaFormChoice, self).__init__(*args, **kwargs)
        choices = [("opcion_{}".format(opcion.pk), opcion.eleccion) for opcion in encuesta.opcion_set.all()]
        self.fields['answer'].choices = [("", "(No votar)")] + choices
