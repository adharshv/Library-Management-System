import os
import shutil

import datetime
from django.db import migrations, models
import django.db.models.deletion

apps=[
    'author',
    'book',
    'book_author',
    'borrower',
    'book_loan',
    'fine',
    'book_search',
    'book_return'
]

for k in apps:
        del_path = os.path.join(os.path.join(os.getcwd(), k), "migrations")
        del_cache_path = os.path.join(os.path.join(os.getcwd(), k), "__pycache__")
        if os.path.exists(del_path):
                shutil.rmtree(del_path)
                shutil.rmtree(del_cache_path)

        # migrations.DeleteModel(k)