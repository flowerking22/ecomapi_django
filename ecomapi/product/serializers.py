from rest_framework import serializers
from .models import productmodel
class productserializer(serializers.ModelSerializer):
    class Meta:
        model=productmodel
        exclude=['productid']
class productupdateserializer(serializers.ModelSerializer):
    class Meta:
        model=productmodel
        exclude=['productid','img','spec2']