# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class MensualidadInline(admin.TabularInline):
    model = models.Mensualidad
    extra = 0


class PagoAdmin(admin.ModelAdmin):
    inlines = [MensualidadInline, ]


admin.site.register(models.Pago, PagoAdmin)
admin.site.register(models.FormaPago)
admin.site.register(models.CuotaPeriodica)
