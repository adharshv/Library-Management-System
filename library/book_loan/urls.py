from django.contrib import admin
from django.urls import include, path

from book_loan import views

urlpatterns = [
    path('', views.index, name='book_loan_index'),
    path('create', views.create, name='book_loan_create'),
    path('new/<slug:isbn>', views.new, name='book_loan_new'),
    path('return/<slug:isbn>', views.return1, name='book_loan_return'),
    
]