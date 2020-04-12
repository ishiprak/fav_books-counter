from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    amazon_url = models.URLField()
