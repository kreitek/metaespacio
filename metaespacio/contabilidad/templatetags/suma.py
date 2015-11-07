# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Library

register = Library()

# Poner context a secas no funciona y es necesario poner context.dicts[0]
# ya que la existencia de block anidados (un bucle for es otro block) hace
# que se genere un tag distinto en el bucle que no tiene relacion con el
# de fuera

# visto en dos sitios:
# http://stackoverflow.com/questions/2077050/django-templatetag-scope-forcing-me-to-do-extra-queries
# http://stackoverflow.com/questions/2566265/is-there-a-django-template-tag-that-lets-me-set-a-context-variable

# fuente original (caida):
# http://od-eon.com/blogs/liviu/scope-variables-template-blocks/


@register.simple_tag(takes_context=True)
def suma_add(context, key, value):
    if key not in context.dicts[0]:
        context.dicts[0][key] = value
    else:
        context.dicts[0][key] += value
    return ''


@register.simple_tag(takes_context=True)
def suma_ver(context, key):
    return str(context.dicts[0].get(key, ''))
