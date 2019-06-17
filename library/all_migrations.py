#!/usr/bin/env python
import os
import sys

args=["python", "makemigrations"]
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

args2=["python", "migrate"]
    
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    for app in apps:
        argsnow = args+[app,]
        execute_from_command_line(argsnow)
    execute_from_command_line(args2)