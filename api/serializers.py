from rest_framework import serializers
from app1.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'genre', 'author', 'isbn')
