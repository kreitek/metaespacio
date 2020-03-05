from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^lineas/$', v.LineaList.as_view(), name="lineas"),
    url(r'^lineas/usuario/(?P<username>[\w_-]+)$', v.LineasUsuario.as_view(), name="lineas_usuario"),
    url(r'^cuentas/$', v.CuentasList.as_view(), name="cuentas"),
    url(r'^cuentas/(?P<pk>\d+)$', v.LineasCuenta.as_view(), name="lineas_cuenta"),
    url(r'^resumen$', v.ResumenPorMeses.as_view(), name="resumen"),
    url(r'^ledger$', v.Ledger.as_view(), name="ledger"),
    url(r'^oficial/$', v.Oficial.as_view(), name="oficial"),
    url(r'^oficial/(?P<year>\d+)$', v.Oficial.as_view(), name="oficial_year"),
]
