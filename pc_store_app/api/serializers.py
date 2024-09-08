from rest_framework import serializers
from pc_store_app.models import Computer

class ComputerSerializer(serializers.Serializer): 
    model = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.IntegerField()
    is_active = serializers.BooleanField()
    
    def create(self, validated_data): 
        return Computer.objects.create(**validated_data)
    
    def update(self, instance, validated_data): 
        instance.model = validated_data.get('model', instance.model)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.price = validated_data.get('price', instance.price)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance