from django.urls import path
from phone_store_app.api.views import phone_list, phone_detail

urlpatterns = [
    path('list/', phone_list , name='phone list'), 
    path('<int:pk>', phone_detail, name='phone detail')
]