from django.shortcuts import render
from pc_store_app.models import Computer
from django.http import JsonResponse

# Create your views here.
def pc_list(request): 
    computer_list = Computer.objects.all()
    data = { 
        "data": list(computer_list.values())    
            }
    
    return JsonResponse(data)