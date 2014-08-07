from django.contrib import admin
from .models import Espacio, MiembroEspacio


class MiembroEspacioInline(admin.TabularInline):
    model = MiembroEspacio
    extra = 0


class EspacioAdmin(admin.ModelAdmin):
    inlines = [MiembroEspacioInline, ]

admin.site.register(Espacio, EspacioAdmin)
