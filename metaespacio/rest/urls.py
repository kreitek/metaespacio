from django.conf.urls import url, include
from rest_framework import routers
from . import views as v

router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'groups', v.GroupViewSet)
router.register(r'miembros', v.MiembroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^spaceapi/', v.spaceapi),

]
