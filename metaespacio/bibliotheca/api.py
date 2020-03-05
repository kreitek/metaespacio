import json

from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource, fields
from .models import Book, Publisher


class PrettyJSONSerializer(Serializer):
    json_indent = 4

    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return json.dumps(
            data,
            cls=DjangoJSONEncoder,
            sort_keys=True,
            ensure_ascii=False,
            indent=self.json_indent
            )


class PublisherResource(ModelResource):
    class Meta:
        queryset = Publisher.objects.all()
        resource_name = 'publisher'
        serializer = PrettyJSONSerializer()

    def determine_format(self, request):
        return 'application/json'


class BookResource(ModelResource):
    publisher = fields.ForeignKey(PublisherResource, 'publisher')

    def determine_format(self, request):
        return 'application/json'

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        serializer = PrettyJSONSerializer()


class BooksResource(ModelResource):
    def determine_format(self, request):
        return 'application/json'

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        list_allowed_methods = ['get', 'head']
        excludes = ['digest', 'cover', 'url']
        serializer = PrettyJSONSerializer()
