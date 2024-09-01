from rest_framework import serializers
from phone_store_app.models import Phone

class PhoneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # price = serializers.IntegerField()
    brand = serializers.CharField()
    model = serializers.CharField()
    
    def create(self, data): 
        return Phone.objects.create(**data)