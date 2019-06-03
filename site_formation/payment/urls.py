from django.urls import path, include
from .views import checkout



app_name='payment'

urlpatterns = [
    path('',checkout, name='checkout'),


    ]