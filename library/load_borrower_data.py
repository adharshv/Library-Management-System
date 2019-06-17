

# main
import os
import django
import library
os.environ['DJANGO_SETTINGS_MODULE']='library.settings'

from django.db import models
django.setup()

import sys
sys.path.append("C:/Users/adhar/Desktop/mylibrary/")

# your imports, e.g. Django models
from borrower.models import borrower

file_pointer = open('borrowers.csv', 'r') # Make a read only connection to the file



list1 = []
data = file_pointer.readlines()
#print(data)
n=1

sql_reset_for_violating_autofield = '''
SELECT MAX(id) FROM your_table;
SELECT nextval('your_table_id_seq');
BEGIN;
LOCK TABLE your_table IN EXCLUSIVE MODE;
SELECT setval('your_table_id_seq', COALESCE((SELECT MAX(id)+1 FROM your_table), 1), false);
COMMIT;
'''
for eachline in data:
    if n==1:
        n=0
        continue
    #print(eachline)
    list1 = []
    list1.append(eachline.split(',')) # each word in each line as list elements here

    card_id = list1[0][0]
    # print(card_id)

    pieces = list1[0][1].split('-')
    # print(pieces)

    ssn=''
    for piece in pieces:
        ssn += piece
    # print(ssn)

    bname = (list1[0][2]+' '+list1[0][3])
    # print(bname)

    address = (list1[0][5]+' '+list1[0][6]+' '+list1[0][7])

    first =  (list1[0][8].split('('))
    # print(first)
    second = ((first[1]).split(')'))  # ['469', ' 904-1438\n']
    # b=borrower(card_id = list1[0], ssn
    # print(list1)
    third = (second[1].strip()) # 904-1438
    fourth = third.split('-') # ['904', '1438']
    
    phone = second[0] + fourth[0] + fourth[1] 
    # print(phone)

    a = borrower(card_id = card_id, ssn = ssn, bname = bname, address = address, phone = phone)
    a.save()
    
    
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("select setval('borrower_borrower_card_id_seq', (select MAX(card_id)+1 from borrower_borrower), false);")



