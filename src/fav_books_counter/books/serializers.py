from rest_framework import serializers
from .models import Book

class BookSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Book
    fields = (
        'title',
        'author',
        'genre',
        'amazon_url',
    )
    