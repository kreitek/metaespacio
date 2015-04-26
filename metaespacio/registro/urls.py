from django.conf.urls import patterns, url

from .views import CreateUser, DetailUser

urlpatterns = patterns(
    '',
    url(r'^create$', CreateUser.as_view(), name="create_user"),
    url(r'^(?P<slug>\w+)$', DetailUser.as_view(slug_field="username"), name="detail_user"),
    # url(r'^show/(?P<pk>\d+)/$', DetailUser.as_view(), name="detail_user"),
)
