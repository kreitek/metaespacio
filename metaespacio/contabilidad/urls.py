from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^lineas/$', v.LineaList.as_view(), name="lineas"),
    url(r'^lineas/usuario/(?P<username>[\w_-]+)$', v.LineasUsuario.as_view(), name="lineas_usuario"),
    url(r'^cuentas/$', v.CuentasList.as_view(), name="cuentas"),
    url(r'^cuentas/(?P<pk>\d+)$', v.LineasCuenta.as_view(), name="lineas_cuenta"),
    url(r'^ledger$', v.Ledger.as_view(), name="ledger"),
)
