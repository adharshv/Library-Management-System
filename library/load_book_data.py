

# main
import os
import django
import library
os.environ['DJANGO_SETTINGS_MODULE']='library.settings'

from django.db import models
django.setup()

import sys
sys.path.append("C:/Users/adhar/Desktop/mylibrary/")

from book.models import book
from author.models import author
from book_author.models import book_author

import csv 
import sys

n=1
 
with open('books.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if n==1:
            n=0
            continue

        isbn = row[1]

        title = row[2]

        name = []
        for eachname in row[3].split(','):
            # print(eachname)
            name.append(eachname)

        # print(name)

        # break

        a = book(title = title, isbn = isbn)
        a.save()

        for i in range(0,len(name)):
            # print(name[i])
            b = author(name = name[i])
            b.save()
            c = book_author(book = a, author = b)
            c.save()
            
        

      

        





