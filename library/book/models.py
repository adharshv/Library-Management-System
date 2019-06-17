from django.db import models

from author.models import author
from django.core.validators import RegexValidator

# Create your models here.
class book(models.Model):
    # isbn=models.CharField(max_length = 13, primary_key=True )
    isbn=models.CharField(
        max_length = 13, primary_key=True,
        validators=[RegexValidator(regex='^\d{13}$', message='Length has to be 13', code='nomatch')],
        )
    title=models.CharField(max_length = 300)
    avail=models.BooleanField(default=True)
    
    def authors(self):
        return [k.author for k in self.book_author_set.all()]
