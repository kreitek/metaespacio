# Create your views here.

from django.views.generic.list import ListView

from .models import Book

class LastestBooks(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.all().order_by('-entry_date')[0:12]
