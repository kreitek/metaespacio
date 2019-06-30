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
        "logo": "https://metaespacio.kreitek.org/static/rest/logo.png",
        "url": "https://kreitek.org",
        "location": {
            "address": "Instituto Nuryana, Camino San Francisco de Paula 64 planta -2, San Cristobal de La Laguna, Santa Cruz de Tenerife, Spain",
            "lon": 28.480287,
            "lat": -16.323105
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
                "open": "https://metaespacio.kreitek.org/static/rest/open.jpg",
                "closed": "https://metaespacio.kreitek.org/static/rest/closed.jpg"
            },
            "open": None
        },
        "projects": [
            "https://wiki.kreitek.org",
            "https://github.com/kreitek"
        ]
    }
    response = JsonResponse(context)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "900"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
