from rest_framework.decorators import api_view
from pc_store_app.models import Computer
from pc_store_app.api.serializers import ComputerSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def computer_list(request): 
    
    if request.method == 'GET': 
        computer_list = Computer.objects.all()
        computer_list_serializer = ComputerSerializer(computer_list, many=True)
        return Response({ "data": computer_list_serializer.data }, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'DELETE'])
def computer_detail(request, pk): 
    
    print(request.data)
    if request.method == 'DELETE': 
        computer = Computer.objects.get(pk=pk)
        computer.delete()
        return Response({"data": "product deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT': 
        computer_instance = Computer.objects.get(pk=pk)
        computer_update_serializer = ComputerSerializer(computer_instance, data=request.data)
        if computer_update_serializer.is_valid(): 
            computer_update_serializer.save()
            return Response({"data": "product updated succesfully"}, status=status.HTTP_201_CREATED)

    computer = Computer.objects.get(pk=pk)
    computer_serializer = ComputerSerializer(computer)
    return Response({ "data": computer_serializer.data }, status=status.HTTP_201_CREATED)

    