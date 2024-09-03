from rest_framework import serializers
from headphone_store_app.models import Headphone

class Headphone_serializer(serializers.Serializer): 
    brand = serializers.CharField()
    model = serializers.CharField()
    price = serializers.IntegerField()
    is_active = serializers.BooleanField()
    stock = serializers.IntegerField()
    description = serializers.CharField()
    
    def create(self, data): 
        return Headphone.objects.create(**data)