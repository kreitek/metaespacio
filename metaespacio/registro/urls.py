from django.conf.urls import patterns, include, url

from .views import CreateUser, DetailUser

urlpatterns = patterns('',
    url(r'^create(.html)?$', CreateUser.as_view(), name="create_user"),
    url(r'^show/(?P<pk>\d+)/$', DetailUser.as_view(), name="detail_user"),
    url(r'^$', CreateUser.as_view(), name="create_user"),
)
