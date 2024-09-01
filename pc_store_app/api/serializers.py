from rest_framework import serializers

class ComputerSerializer(serializers.Serializer): 
    model = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.IntegerField()
    is_active = serializers.BooleanField()