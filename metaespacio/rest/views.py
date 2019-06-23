from django.contrib.auth.models import User, Group
from django.http import JsonResponse

from espacios.models import Miembro
from rest_framework import viewsets
from .serializers import MiembroSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MiembroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows miembros to be viewed or edited.
    """
    queryset = Miembro.objects.all().order_by('-fecha_alta')
    serializer_class = MiembroSerializer

def spaceapi(request):
    # https://spaceapi.io/
    # TODO esta hardcodeado para probar, pasar a DB o a settings
    context = {
      "api": "0.13",
      "space": "Kreitek",
      "logo": "https://kreitek.org//sites/default/files/kreitek_imagen.jpg",
      "url": "https://kreitek.org",
      "location": {
        "address": "Colegio Nuryana, Calle San Francisco de Paula, San Cristobal de La Laguna, Santa Cruz de Tenerife, Spain",
        "lon": 28.4787801,
        "lat": -16.3256688
      },
      "contact": {
        "email": "info@kreitek.org",
        "twitter": "@kreitek"
      },
      "issue_report_channels": [
        "email"
      ],
      "state": {
        "icon": {
          "open": "https://kreitek.org//sites/default/files/site_open.gif",
          "closed": "https://kreitek.org//sites/default/files/site_closed.gif"
        },
        "open": False
      },
      "projects": [
        "https://github.com/kreitek",
        "https://wiki.kreitek.org"
      ]
    }
    return JsonResponse(context)
