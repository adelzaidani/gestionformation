from django.urls import path, include
from .views import print_invoice



app_name='billing'

urlpatterns = [
    path('<int:id_session>/', print_invoice, name='print_invoice'),


    ]