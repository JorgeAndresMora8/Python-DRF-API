from rest_framework.decorators import api_view
from headphone_store_app.models import Headphone
from headphone_store_app.api.serializer import Headphone_serializer
from django.http import JsonResponse
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def headphone_list(request): 
    if request.method == 'POST': 
        data_serialized = Headphone_serializer(data=request.data)
        if data_serialized.is_valid(): 
            data_serialized.save()
            return JsonResponse({"data": "Headphone added succesfully"})
        else: 
            return JsonResponse({"data": "there was an error"})
    
    headphones = Headphone.objects.all()
    headphone_serializers = Headphone_serializer(headphones, many=True)
    return JsonResponse({'data':headphone_serializers.data})


@api_view(['GET', 'PUT', 'DELETE'])
def headphone_detail(request, pk):
    
    if request.method == 'PUT': 
        headphone = Headphone.objects.get(pk=pk)
        headphone_instance = Headphone_serializer(headphone, data=request.data)
        if headphone_instance.is_valid(): 
            headphone_instance.save()
            return JsonResponse({'data': 'headphone updated succesfully'})
        
    if request.method == 'DELETE': 
        return JsonResponse({"data": "product deleted succesfully"})
    
    headphone = Headphone.objects.get(pk=pk)
    headphone_serializer = Headphone_serializer(headphone)
    return JsonResponse({'data': headphone_serializer.data})
    