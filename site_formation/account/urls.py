from django.urls import path, include
from . import views

app_name='account'

urlpatterns = [
    path('sign_up/',views.sign_up,name='sign_up'),


]