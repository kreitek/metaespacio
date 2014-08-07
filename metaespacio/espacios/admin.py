from django.contrib import admin
from .models import Espacio, MiembroEspacio


class MiembroEspacioInline(admin.TabularInline):
    model = MiembroEspacio
    extra = 0


class EspacioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cuenta_miembros']
    inlines = [MiembroEspacioInline, ]

    def cuenta_miembros(self, obj):
        return obj.miembros.count()


admin.site.register(Espacio, EspacioAdmin)
