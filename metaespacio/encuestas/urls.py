from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', v.EncuestaView.as_view(), name="encuesta_view"),
]
