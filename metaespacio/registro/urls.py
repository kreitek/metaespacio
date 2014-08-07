from django.conf.urls import patterns, include, url

from .views import CreateUser

urlpatterns = patterns('',
    url(r'^create.html$', CreateUser.as_view(), name="create_user"),
)
