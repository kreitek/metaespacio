# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import CreateView, DetailView
from common.views import LoginRequiredMixin
from espacios.models import Miembro
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
        messages.success(self.request, 'Creado usuario. El usuario está desactivado hasta que un administrador lo revise. ')
        return redirect_url


class DetailUser(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registro/usuario_detalle.html"
    context_object_name = "this_user"  # importante para no sobreescribir {{user}} de auth

    def dispatch(self, request, *args, **kwargs):
        self.url_user = get_object_or_404(User, username=self.kwargs['slug'])
        self.espacios = get_list_or_404(Miembro, user=self.request.user.pk)
        return super(DetailUser, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailUser, self).get_context_data(**kwargs)
        context[self.context_object_name] = self.url_user
        context['espacios'] = self.espacios
        return context