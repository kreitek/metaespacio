# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template import Library
from django.core.urlresolvers import reverse

register = Library()


@register.simple_tag(takes_context=True)
def admin(context, *objs):
    out = ""
    if "user" in context and context["user"].is_superuser:
        for obj in objs:
            if isinstance(obj, str) or isinstance(obj, unicode):
                if obj:
                    app, model = obj.split("_", 1)
                    url = reverse('admin:{}_{}_add'.format(app, model))
                    out += '<a href="{}" target="admin" title="new {}" class="pull-right"><span class="glyphicon glyphicon-plus"></span></a>'.format(url, model)
            else:
                app = obj.__class__.__module__.split(".")[-2]
                model = obj.__class__.__name__.lower()
                url = reverse('admin:{}_{}_change'.format(app, model), args=[obj.pk])
                out += '<a href="{}" target="admin" title="edit {} (pk={})" class="pull-right"><span class="glyphicon glyphicon-pencil"></span></a>'.format(url, model, obj.pk)
    return out
