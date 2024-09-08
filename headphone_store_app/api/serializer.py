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
    
    def update(self, instance, validated_data): 
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.price = validated_data.get('price', instance.price)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
        