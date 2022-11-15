from django.contrib import admin
from django.urls import path, include
from sales.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('mobil/', include('mobil.urls')),
]
