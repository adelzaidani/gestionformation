from django.urls import path, include
from .views import print_invoice


app_name='billing'

urlpatterns = [
    path('',print_invoice,name='invoice'),
    ]