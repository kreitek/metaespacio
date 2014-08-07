from django.shortcuts import render
from django.views.generic import CreateView

from .models import Usuario
from .forms import UsuarioForm

class CreateUser(CreateView):
    model = Usuario
    form_class = UsuarioForm

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        self.object.is_active = False
        self.object.save()
        return redirect_url
