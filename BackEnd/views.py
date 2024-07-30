from django.shortcuts import render
from . serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
from . models import Author, Book

#Author serializer views
class AuthorListCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
#Book serializer views
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    