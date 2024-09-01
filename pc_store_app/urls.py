from django.urls import path
from pc_store_app.views import pc_list

urlpatterns = [
    path('list/', pc_list , name='pc list')
]
