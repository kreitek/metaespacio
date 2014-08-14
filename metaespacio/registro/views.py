# -*- coding: utf-8 -*-

from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import UsuarioForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CreateUser(CreateView):
    model = Usuario
    form_class = UsuarioForm

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        # FIXME usar Django-registration http://django-registration.readthedocs.org/
        # self.object.is_active = False
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()
        return redirect_url


class DetailUser(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = "registro/usuario_detalle.html"
