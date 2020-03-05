from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^members$', v.ListMember.as_view(), name="list_member"),
]
