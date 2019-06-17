from django.contrib import admin
from django.urls import include, path

from borrower import views

urlpatterns = [
    path('', views.index, name='borrower_index'),
    path('new', views.new, name='borrower_new'),
    path('create', views.create, name='borrower_create'),
    path('<slug:card_id>', views.view, name='borrower_view'),
]