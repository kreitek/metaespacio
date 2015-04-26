# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, DetailView
# from .models import DatosPersonales
from .forms import UserForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    success_url = "/"

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        # FIXME usar Django-registration http://django-registration.readthedocs.org/
        self.object.is_active = False
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()
        messages.success(self.request, 'Creado usuario. El usuario está desactivado hasta que un administrador lo revise. ')
        return redirect_url


class DetailUser(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registro/usuario_detalle.html"
