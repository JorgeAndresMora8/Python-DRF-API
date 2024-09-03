from django.urls import path
from headphone_store_app.api.views import headphone_list

urlpatterns = [
    path('list/', headphone_list, name='headphone list')
]
