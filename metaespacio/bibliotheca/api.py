#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource, fields
from .models import Book, Publisher

class PublisherResource(ModelResource):
    class Meta:
        queryset = Publisher.objects.all()
        resource_name = 'publisher'

    def determine_format(self, request):
        return 'application/json'

class BookResource(ModelResource):

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book' 

    publisher = fields.ForeignKey(PublisherResource, 'publisher')

    def determine_format(self, request):
        return 'application/json'