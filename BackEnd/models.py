import datetime
from django.db import models
from django.forms import ValidationError


#Validators
def validate_year(value):
    current_year = datetime.date.today().year
    if value < 1800 or value > current_year:
        raise ValidationError(f"{value} is not a valid year. Year must be between 1900 and {current_year}.")


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    country = models.CharField(max_length=100, null=False)
    
    @property 
    def complete_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.complete_name
    
class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    genre = models.CharField(max_length=50, null=False)
    synopsis = models.TextField()
    release_date = models.IntegerField(validators=[validate_year])
    
    def __str__(self):
        return self.title