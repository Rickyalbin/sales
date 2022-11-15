from django.urls import path
from mobil.views import *

urlpatterns = [
    path('list', mobil_list, name='mobil_list'),
    path('add', mobil_add, name='mobil_add'),
    path('update\<int:id>', mobil_update, name='mobil_update'),
    path('delete\<int:id>', mobil_delete, name='mobil_delete'),
]
