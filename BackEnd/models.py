from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=100, null=False)
    
    name = first_name, last_name
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    genre = models.CharField(max_length=50, null=False),
    synopsis = models.TextField()
    
    def __str__(self):
        return self.title