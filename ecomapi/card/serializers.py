from rest_framework import serializers
from .models import cardmodel
class cardserializer(serializers.ModelSerializer):
    class Meta:
        model=cardmodel
        exclude=['id']