from django.contrib import admin
from .models import Espacio, Miembro


class MiembroInline(admin.TabularInline):
    model = Miembro
    extra = 0


class EspacioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cuenta_miembros', 'site']
    inlines = [MiembroInline, ]

    def cuenta_miembros(self, obj):
        return obj.miembros.count()


class MiembroAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'fecha_alta']
    list_filter = ['espacio']

admin.site.register(Espacio, EspacioAdmin)
admin.site.register(Miembro, MiembroAdmin)
