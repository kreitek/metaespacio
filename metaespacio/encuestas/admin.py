from django.contrib import admin
from . import models


class OpcionInline(admin.TabularInline):
    model = models.Opcion
    extra = 0


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'opcion_count', 'voto_count', 'voto_multiple', 'voto_editable', 'voto_anonimo']
    list_filter = ['espacio']
    inlines = [OpcionInline, ]


admin.site.register(models.Encuesta, EncuestaAdmin)
admin.site.register(models.Voto)
