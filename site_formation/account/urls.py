from django.urls import path, include
from .views import sign_up,editProfile, password_change
from django.contrib.auth.views import LoginView,LogoutView

app_name='account'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sign_up/',sign_up,name='sign_up'),
    path('profile/edit',editProfile, name="edit_profile"),
    path('profile/change_password',password_change,name='change_password')
]