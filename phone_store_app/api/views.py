from phone_store_app.models import Phone
from django.http import JsonResponse
from phone_store_app.api.serializers import PhoneSerializer
from rest_framework.decorators import api_view

# Create your views here.
api_view()
def phone_list(request):
    phones = Phone.objects.all()
    
    phones_serializer = PhoneSerializer(phones, many=True)
    print(phones_serializer.data)
    return JsonResponse({"data": phones_serializer.data})

api_view()
def phone_detail(request, pk): 
    phone_detail = Phone.objects.get(pk=pk)
    phone_serializer = PhoneSerializer(phone_detail)
    
    return JsonResponse({ "data": phone_serializer.data })