from django.urls import path
from . import views
urlpatterns=[
      path('',views.index),
    path('<str:email>',views.getone),
    path('<str:email>/<str:name>',views.modifyone)
]