from django.db import models

# Create your models here.
class author(models.Model):
    author_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 120)
    
    def books(self):
        return [k.book for k in self.book_author_set.all()]