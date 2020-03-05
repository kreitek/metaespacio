from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import DatosPersonales
from caronte.models import Autorizacion


class DatosPersonalesInline(admin.StackedInline):
    model = DatosPersonales


class AutorizacionInline(admin.StackedInline):
    model = Autorizacion
    extra = 0


class UserAdmin2(UserAdmin):
    inlines = UserAdmin.inlines + [DatosPersonalesInline, AutorizacionInline]
    list_filter = ('espacio', ) + UserAdmin.list_filter


admin.site.unregister(User)
admin.site.register(User, UserAdmin2)
