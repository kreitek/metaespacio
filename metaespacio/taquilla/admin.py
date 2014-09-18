from django.contrib import admin

from .models import Taquillero, Taquilla, AbonoTaquilla


class TaquilleroAdmin(admin.ModelAdmin):
    pass


class AbonoTaquillaInline(admin.TabularInline):
    model = AbonoTaquilla


class TaquillaAdmin(admin.ModelAdmin):
    inlines = [AbonoTaquillaInline, ]


admin.site.register(Taquillero, TaquilleroAdmin)
admin.site.register(Taquilla, TaquillaAdmin)
