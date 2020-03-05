from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^(?P<lector_slug>.*)/(?P<codigo>.*)', v.lector_codigo),
    url(r'^(?P<lector_slug>.*)', v.lector_keepalive),
]
