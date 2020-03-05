from django.contrib.auth.models import User, Group
from espacios.models import Miembro
from rest_framework import serializers
from contabilidad.models import Linea
from django.db.models import Sum
from django.utils.timezone import now
from django.db.models import Q


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MiembroSerializer(serializers.HyperlinkedModelSerializer):
    espacio = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='slug'
    )
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )
    ha_pagado_este_mes = serializers.SerializerMethodField()
    es_socio = serializers.BooleanField(read_only=True,)

    def get_ha_pagado_este_mes(self, obj):
        pagado = Linea.objects.filter(miembro=obj) \
            .filter((Q(fecha__year=now().year) &
                     Q(fecha__month=now().month)) |
                    (Q(asiento__fecha__year=now().year) &
                     Q(asiento__fecha__month=now().month)))
        pagado_m = pagado.filter(cuenta__in=obj.espacio.cuotas.filter(signo='-'))\
            .aggregate(Sum('cantidad'))['cantidad__sum']
        if not pagado_m:
            pagado_m = 0
        pagado = pagado.filter(cuenta__in=obj.espacio.cuotas.filter(signo='+'))\
            .aggregate(Sum('cantidad'))['cantidad__sum']
        if not pagado:
            pagado = 0

        return pagado - pagado_m

    class Meta:
        model = Miembro
        fields = ('url', 'espacio', 'user', 'ha_pagado_este_mes', 'es_socio')
