from phone_store_app.models import Phone
from django.http import JsonResponse
from phone_store_app.api.serializers import PhoneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def phone_list(request):
    
    if request.method == 'POST': 
        phone_serialized = PhoneSerializer(request.data)
        if phone_serialized.is_valid(): 
            phone_serialized.save()
            return Response({"data": "phone added succesfully"}, status=status.HTTP_201_CREATED)
        
        
        
    phones = Phone.objects.all()
    phones_serializer = PhoneSerializer(phones, many=True)
    return Response({"data": phones_serializer.data})



api_view(['GET', 'PUT', 'DELETE'])
def phone_detail(request, pk): 
    
    if request.method == 'PUT': 
        phone_instance = Phone.objects.get(pk=pk)
        phone_serialized = PhoneSerializer(phone_instance, data=request.data)
        if phone_serialized.is_valid(): 
            phone_serialized.save()
            return Response({"data": "phone updated succesfully"}, status=status.HTTP_201_CREATED)
        
    if request.method == 'DELETE': 
        phone = Phone.objects.get(pk=pk)
        phone.delete()
        return Response({"data": "product deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
   
    
    phone_detail = Phone.objects.get(pk=pk)
    phone_serializer = PhoneSerializer(phone_detail)
    return JsonResponse({ "data": phone_serializer.data })