from rest_framework.decorators import api_view
from headphone_store_app.models import Headphone
from headphone_store_app.api.serializer import Headphone_serializer
from django.http import JsonResponse
from rest_framework.response import Response


api_view(['GET', 'POST'])
def headphone_list(request): 
    if request.method == 'GET':
        return JsonResponse({"data": 'headphone list'})
    
    if request.method == 'POST': 
        print(request.data)
        return JsonResponse({"data": 'headphone list'})
