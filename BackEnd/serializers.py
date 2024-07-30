from rest_framework import serializers
from . models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", 'first_name', 'last_name', 'country']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"