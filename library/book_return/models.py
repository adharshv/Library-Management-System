from django.db import models

# Create your models here.
class book_return(models.Model):
    
    Borrower_ID_name_or_ISBN = models.CharField(max_length = 100)