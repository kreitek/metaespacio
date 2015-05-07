# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from espacios.models import Miembro
from .forms import EncuestaFormChoice, EncuestaFormMulti
from .models import Encuesta, Voto


class EncuestaView(FormView):
    template_name = "encuestas/encuesta_detail.html"
    success_url = "."

    def dispatch(self, request, *args, **kwargs):
        self.site = get_current_site(request)
        self.encuesta = get_object_or_404(Encuesta, espacio__site=self.site, pk=kwargs['pk'])
        self.miembro = get_object_or_404(Miembro, user=self.request.user.pk, espacio=self.encuesta.espacio)
        self.qs_votos = self.miembro.voto_set.filter(opcion__encuesta=self.encuesta)
        return super(EncuestaView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EncuestaView, self).get_context_data(**kwargs)
        context['object'] = self.encuesta
        context['mis_votos'] = self.qs_votos.all()
        return context

    def get_form_class(self):
        return EncuestaFormMulti if self.encuesta.voto_multiple else EncuestaFormChoice

    def get_form_kwargs(self):
        kwargs = super(EncuestaView, self).get_form_kwargs()
        kwargs['encuesta'] = self.encuesta
        return kwargs

    def get_initial(self):
        initial = super(EncuestaView, self).get_initial()
        if self.encuesta.voto_multiple:
            for voto in self.qs_votos.all():
                initial["opcion_{}".format(voto.opcion.pk)] = True
        elif self.qs_votos.count():
            voto = self.qs_votos.first()
            initial['answer'] = "opcion_{}".format(voto.opcion.pk)
        return initial

    def form_valid(self, form):
        url = super(EncuestaView, self).form_valid(form)
        qs_opciones = self.encuesta.opcion_set.all()

        if not self.encuesta.voto_editable and self.qs_votos.count():
            messages.error(self.request, 'Ya votó')
            return url

        if self.encuesta.finalizada:
            messages.error(self.request, 'Encuesta finalizada')
            return url

        self.qs_votos.delete()

        vote = False
        if self.encuesta.voto_multiple:
            for answer, value in form.cleaned_data.items():
                if answer.startswith("opcion_") and value:
                    pk = answer.replace("opcion_", "")
                    opcion = qs_opciones.get(pk=pk)
                    Voto.objects.create(miembro=self.miembro, opcion=opcion)
                    messages.success(self.request, 'Registrado voto opcion {}'.format(opcion.eleccion))
                    vote = True
        else:
            pk = form.cleaned_data['answer'].replace("opcion_", "")
            if pk:
                opcion = qs_opciones.get(pk=pk)
                Voto.objects.create(miembro=self.miembro, opcion=opcion)
                messages.success(self.request, 'Registrado voto opcion {}'.format(opcion.eleccion))
                vote = True
        if not vote:
            messages.success(self.request, 'No vota')
        return url
