from django.urls import path, include
from .views import sign_up ,MyProfile, ProfileUpdate

app_name='account'

urlpatterns = [
    path('sign_up/',sign_up,name='sign_up'),
    path('profile/',MyProfile.as_view(), name="my_profile"),
    path('profile/update',ProfileUpdate.as_view(), name="profile_update"),


]