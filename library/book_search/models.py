from django.db import models

# Create your models here.
class book_search(models.Model):
    
    ISBN_title_or_author=models.CharField(max_length = 100)