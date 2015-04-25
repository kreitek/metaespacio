# FIXME esto esta sin probar, no funcionaba en django 1.8 por el tastypie

from tastypie.api import Api
from bibliotheca import api

v1_api = Api(api_name='v1')
v1_api.register(api.BookResource())
v1_api.register(api.PublisherResource())
v1_api.register(api.BooksResource())
