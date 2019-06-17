#!/bin/bash
apps=(
    'author'
    'book'
    'book_author'
    'borrower'
    'book_loan'
    'fine'
    'book_search'
    'book_return'
);

for app in apps
do
    python manage.py makemigrations $app

done