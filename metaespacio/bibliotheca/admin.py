#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
import models

admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Publisher)
admin.site.register(models.Authorship)


