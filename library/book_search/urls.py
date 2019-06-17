from django.contrib import admin
from django.urls import include, path

from book_search import views

urlpatterns = [
    path('', views.index, name='book_search_index'),
    path('results',views.results, name='book_search_results'),
    
    
]