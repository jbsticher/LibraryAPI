from django.views.generic import ListView
from .models import Book


class HomePageView(ListView):
    template_name = 'app1/home.html'
    model = Book

