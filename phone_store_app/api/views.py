from phone_store_app.models import Phone
from django.http import JsonResponse
from phone_store_app.api.serializers import PhoneSerializer
from rest_framework.decorators import api_view

# Create your views here.
api_view(['GET', 'POST'])
def phone_list(request):
    
    print(request.method)
    if request.method == 'GET':
        phones = Phone.objects.all()
        phones_serializer = PhoneSerializer(phones, many=True)
        return JsonResponse({"data": phones_serializer.data})

    if request.method == 'POST': 
        print(request.data)
        # phone_serializer = PhoneSerializer(data=request.data)
        # if phone_serializer.is_valid(): 
            # phone_serializer.save()
        return JsonResponse({ "message": "Phone created successfully" })


api_view()
def phone_detail(request, pk): 
    phone_detail = Phone.objects.get(pk=pk)
    phone_serializer = PhoneSerializer(phone_detail)
    
    return JsonResponse({ "data": phone_serializer.data })