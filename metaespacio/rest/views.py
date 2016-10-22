from django.contrib.auth.models import User, Group
from espacios.models import Miembro
from rest_framework import viewsets
from serializers import MiembroSerializer, UserSerializer, GroupSerializer


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

