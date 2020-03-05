from django.conf.urls import url
from .views import LastestBooks

urlpatterns = [
    url(r'^$', LastestBooks.as_view()),
]
