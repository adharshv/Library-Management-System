from django.contrib import admin
from django.urls import include, path

from author import views

urlpatterns = [
    path('', views.index, name='author_index'),
    path('new', views.new, name='author_new'),
    path('create', views.create, name='author_create'),
    path('<int:author_id>', views.view, name='author_view'),
]
