# from django.shortcuts import render
# from phone_store_app.models import Phone
# from django.http import JsonResponse

# # Create your views here.
# def phone_list(request):
#     phones = Phone.objects.all()
#     data = {"data": list(phones.values())}
    
#     return JsonResponse(data)

# def phone_detail(request, pk): 
#     phone_detail = Phone.objects.get(pk=pk)
#     data = {
#         'model': phone_detail.model, 
#         'brand': phone_detail.brand, 
#         'description': phone_detail.description, 
#      }
    
#     return JsonResponse(data)