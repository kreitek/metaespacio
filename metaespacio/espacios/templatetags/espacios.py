# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Library
from ..models import Espacio

register = Library()


@register.inclusion_tag('espacios/_otros_espacios.html', takes_context=True)
def otros_espacios(context):
    qs = Espacio.objects.all()
    if 'espacio' in context:
        qs = qs.exclude(pk=context['espacio'].pk)
    return {'otros_espacios': qs}
