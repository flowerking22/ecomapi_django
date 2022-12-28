from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('all',views.getall),
path('<str:name>',views.getone),
path('create',views.create)
]