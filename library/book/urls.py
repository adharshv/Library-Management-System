from django.contrib import admin
from django.urls import include, path

from book import views

urlpatterns = [
    path('', views.index, name='book_index'),
    path('new', views.new, name='book_new'),
    path('create', views.create, name='book_create'),
    path('<slug:isbn>', views.view, name='book_view'),
]
