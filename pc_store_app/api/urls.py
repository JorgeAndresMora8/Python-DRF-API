from django.urls import path
from pc_store_app.api.views import computer_list, computer_detail

urlpatterns = [
    path('list/', computer_list , name='pc list'), 
    path('<int:pk>', computer_detail, name='pc detail')
]
