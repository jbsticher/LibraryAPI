from app1.models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

