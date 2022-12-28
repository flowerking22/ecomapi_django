from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.user),
    path('login/',views.login),
    path('address/',views.address),
    path('addressuser/<str:email>',views.addressuser)
]