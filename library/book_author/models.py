from django.db import models

from author.models import author
from book.models import book

# Create your models here.
class book_author(models.Model):
    author = models.ForeignKey(author, on_delete = models.CASCADE, db_column="author_id")
    book = models.ForeignKey(book, on_delete = models.CASCADE, db_column="isbn")

    class Meta:
        unique_together = (("author", "book"),)