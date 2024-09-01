from rest_framework.decorators import api_view
from pc_store_app.models import Computer
from pc_store_app.api.serializers import ComputerSerializer
from django.http import JsonResponse

api_view(['GET', 'POST'])
def computer_list(request): 
    
    if request.method == 'GET': 
        computer_list = Computer.objects.all()
        computer_list_serializer = ComputerSerializer(computer_list, many=True)
        return JsonResponse({ "data": computer_list_serializer.data })
    
    if request.method == 'POST': 
        computer_serializer = ComputerSerializer(request.data)
        if computer_serializer.is_valid(): 
            computer_serializer.save()
            return JsonResponse({ "message": "Phone created succesfully" })
        else: 
            return JsonResponse({ "message": "Invalid data, please check the info submited" })

def computer_detail(request, pk): 
    computer = Computer.objects.get(pk=pk)
    computer_serializer = ComputerSerializer(computer)
    return JsonResponse({ "data": computer_serializer.data })