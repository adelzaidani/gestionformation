from django.urls import path, include
from .views import sign_up ,MyProfile,editProfile

app_name='account'

urlpatterns = [
    path('sign_up/',sign_up,name='sign_up'),
    path('profile/',MyProfile.as_view(), name="my_profile"),
    path('profile/edit',editProfile, name="edit_profile"),
]