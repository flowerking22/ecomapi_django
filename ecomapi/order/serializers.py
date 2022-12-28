from rest_framework import serializers
from .models import ordersmodel
class ordersserializer(serializers.ModelSerializer):
    class Meta:
        model=ordersmodel
        exclude=['id']