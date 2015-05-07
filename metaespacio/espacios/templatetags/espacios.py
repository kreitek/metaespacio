# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Library
from ..models import Espacio

register = Library()


@register.inclusion_tag('espacios/_otros_espacios.html', takes_context=True)
def otros_espacios(context):
    qs = Espacio.objects.all()
    if 'espacio' in context:
        obj = context['espacio']
        if obj:
            qs = qs.exclude(pk=obj.pk)
    return {'otros_espacios': qs}
