from rest_framework import serializers
from . import models
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=models.usermodel
        fields=['email','username','password','phone']
class usersignupserializer(serializers.ModelSerializer):
    class Meta:
        model=models.usermodel
        fields=['username','password','phone','email']
class useraddressserializer(serializers.ModelSerializer):
    class Meta:
        model=models.useraddressmodel
        fields='__all__'
"""
class productserializer(serializers.ModelSerializer):
    class Meta:
        model=models.productmodel
        exclude=['productid','img']
class productupdateserializer(serializers.ModelSerializer):
    class Meta:
        model=models.productmodel
        exclude=['productid','img','spec2']
"""
