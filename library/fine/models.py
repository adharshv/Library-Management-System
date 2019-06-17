from django.db import models
from book_loan.models import book_loan
# from django.dispatch import receiver
# from django.core.signals import post_save

# Create your models here.
class fine(models.Model):
    
    book_loan = models.OneToOneField(book_loan, on_delete=models.CASCADE, db_column="loan_id", primary_key=True) #one to one
    
     
    fine_amt = models.DecimalField(default = 0, max_digits= 7, decimal_places=2)
    
    paid = models.BooleanField(blank=False) #True or False

   
    # @receiver(post_save, sender=book_loan,dispatch_uid="create fine")
    # def create_fine(sender, instance, **kwargs):
    #     fine.objects.get_or_create(loan_id=kwargs.get('instance')) 
    