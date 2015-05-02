# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Mensualidad
from espacios.views import SiteMixin


class MensualidadList(SiteMixin, ListView):
    model = Mensualidad

    def get_queryset(self):
        url_user = get_object_or_404(User, username=self.kwargs['username'])
        login_user = self.request.user
        if not login_user.is_superuser and url_user.pk != login_user.pk:
            raise Http404
        return super(MensualidadList, self).get_queryset().filter(
            miembro__user=url_user,
            miembro__espacio__site=self.site)
