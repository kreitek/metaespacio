from django.shortcuts import render
from django.views.generic import CreateView

from .models import EspacioUser
from .forms import EspacioUserForm

class CreateUser(CreateView):
    model = EspacioUser
    form_class = EspacioUserForm

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        self.object.is_active = False
        self.object.save()
        return redirect_url
