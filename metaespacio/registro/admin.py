from django.contrib import admin

from .models import DatosPersonales
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class DatosPersonalesInline(admin.StackedInline):
    model = DatosPersonales

class NewUserAdmin(UserAdmin):
    inlines = [DatosPersonalesInline]


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
