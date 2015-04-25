from django.conf.urls import patterns, url

from .views import CreateUser, DetailUser

urlpatterns = patterns(
    '',
    url(r'^create(.html)?$', CreateUser.as_view(), name="create_user"),
    url(r'^show/(?P<pk>\d+)/$', DetailUser.as_view(), name="detail_user"),
    url(r'^show/username/(?P<slug>\w+)/$', DetailUser.as_view(slug_field="username"), name="detail_username"),
    url(r'^$', CreateUser.as_view(), name="create_user"),
)
