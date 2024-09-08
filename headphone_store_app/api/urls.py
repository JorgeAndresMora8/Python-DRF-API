from django.urls import path
from headphone_store_app.api.views import headphone_list, headphone_detail

urlpatterns = [
    path('list/', headphone_list, name='headphone list'), 
    path('<int:pk>', headphone_detail, name='headphone detail' )
]
