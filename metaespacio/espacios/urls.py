from django.conf.urls import patterns, url
from . import views as v

urlpatterns = patterns(
    '',
    url(r'^members$', v.ListMember.as_view(), name="list_member"),
)
