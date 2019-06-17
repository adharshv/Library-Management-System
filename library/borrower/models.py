from django.db import models

from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from book.models import book
from django.core.validators import RegexValidator

# Create your models here.
class borrower(models.Model):
    

    # card_id = models.CharField(max_length = 6, primary_key=True,
    #     validators=[RegexValidator(regex='^\d{6}$', message='Length has to be 6', code='nomatch')],
    #     )

    # card_id = models.AutoField(max_length = 6, primary_key=True,
    #     validators=[RegexValidator(regex='^\d{6}$', message='Length has to be 6', code='nomatch')],
    #     )

    card_id = models.AutoField(primary_key=True, validators=[MaxLengthValidator(6),MinLengthValidator(6)])





    ssn = models.CharField(max_length = 9, unique=True,
        validators=[RegexValidator(regex='^\d{9}$', message='Length has to be 9', code='nomatch')],
        )

    bname = models.CharField(max_length = 50)
    
    loans = models.IntegerField(default=0,validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ])
    address = models.CharField(max_length = 200)
    
    phone = models.CharField(max_length = 10, 
        validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='nomatch')],
        )

    
    def books(self):
        return [k.book for k in self.book_loan_set.all()]