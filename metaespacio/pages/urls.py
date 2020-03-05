from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)$', v.PaginaView.as_view(), name="pagina_view"),
    url(r'^$', v.PaginaIndex.as_view(), name="inicio"),
]
