from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=30)

    def __str__(self):
        return self.title
