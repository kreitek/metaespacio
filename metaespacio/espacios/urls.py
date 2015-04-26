from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='espacios/inicio.html')),
    url(r'^members$', v.ListMember.as_view(), name="list_member"),
)
