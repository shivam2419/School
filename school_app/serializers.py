from rest_framework import serializers
from .models import *

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = '__all__'