from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^create$', v.CreateUser.as_view(), name="create_user"),
    url(r'^(?P<slug>\w+)$', v.DetailUser.as_view(slug_field="username"), name="detail_user"),
    # url(r'^show/(?P<pk>\d+)/$', DetailUser.as_view(), name="detail_user"),
)
