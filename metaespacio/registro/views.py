# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, DetailView
from common.views import LoginRequiredMixin
from .forms import UserForm


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    success_url = "/"

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        self.object.is_active = False
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()
        messages.success(self.request, 'Creado usuario. El usuario está desactivado ' +
                         'hasta que un administrador lo revise. ')
        return redirect_url


class DetailUser(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registro/usuario_detalle.html"
    context_object_name = "this_user"  # importante para no sobreescribir {{user}} de auth
