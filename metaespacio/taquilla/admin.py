from django.contrib import admin

from .models import Taquillero, Taquilla, Abono


class TaquilleroAdmin(admin.ModelAdmin):
    pass


class AbonoInline(admin.TabularInline):
    model = Abono


class TaquillaAdmin(admin.ModelAdmin):
    inlines = [AbonoInline, ]


admin.site.register(Taquillero, TaquilleroAdmin)
admin.site.register(Taquilla, TaquillaAdmin)
