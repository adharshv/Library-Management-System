from django.db import models
from django.db.models import signals
from datetime import datetime
from datetime import timedelta
from borrower.models import borrower

from book.models import book
import calendar

from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class book_loan(models.Model):
    loan_id = models.AutoField(primary_key=True )
    book = models.OneToOneField(book, on_delete=models.CASCADE, db_column="isbn") # one loan for one book
    borrower = models.ForeignKey(borrower, on_delete=models.CASCADE, db_column="card_id") #many loans to one borrower
    date_out = models.DateTimeField(default=datetime.now)
    date_in = models.DateTimeField(null=True,  blank=True)

    # due_date = date_out + timedelta(days=14)
    due_date = datetime.now() + timedelta(days=14)

    class Meta:
        ordering = ['borrower']
   

    # def save(self, *args, **kwargs):
    #     f=fine(book_loan=self,paid=False)
    #     f.save()
    #     super(book_loan, self).save(*args, **kwargs)


  


    def get_days_passed(self):
        d1 = self.due_date

        if self.date_in is None:
            d2= datetime.now() + timedelta(days=0)
        else:
            d2 = self.date_in + timedelta(days=0)

        # if (d1-d2) < 0: # checked in before due date
        #     return 0 
        # else:
        #     return (d1 - d2).days 
        
        delta = (d2 - d1)
        return delta.days    

