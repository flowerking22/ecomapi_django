from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('p/<int:id>',views.getbyproduct),
    path('u/<str:email>',views.getbyuser),
    path('<int:pid>/<str:email>',views.getonlyone)
]