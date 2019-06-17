from django.contrib import admin
from django.urls import include, path

from fine import views

urlpatterns = [
    path('', views.index, name='fine_index'),
    path('create', views.create, name='fine_create'),
    path('results',views.results, name='fine_results'),
    path('pay/<slug:card_id>', views.pay, name='fine_pay'),
]