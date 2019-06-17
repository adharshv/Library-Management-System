from django.contrib import admin
from django.urls import include, path

from book_return import views

urlpatterns = [
    path('', views.index, name='book_return_index'),
    path('results',views.results, name='book_return_results'),
    
    
]