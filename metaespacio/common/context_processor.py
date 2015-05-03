# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from espacios.models import Espacio

import logging
logger = logging.getLogger(__name__)


def site(request):
    kwargs = {
        'espacios': Espacio.objects.all(),
    }
    try:
        kwargs['site'] = get_current_site(request)
        kwargs['espacio'] = kwargs['site'].espacio_set.first()
    except Site.DoesNotExist:
        kwargs['espacio'] = kwargs['site'] = None
        logger.error("Site does not exist: {}".format(request.get_host()))
    return kwargs
