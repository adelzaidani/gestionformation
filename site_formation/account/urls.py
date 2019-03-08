from django.urls import path, include, reverse_lazy
from .views import sign_up,editProfile, password_change
from django.contrib.auth.views import \
    (LoginView,LogoutView,
     )
from django.contrib.auth import views as auth_views


#app_name='account'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sign_up/',sign_up,name='sign_up'),
    path('profile/edit',editProfile, name="edit_profile"),
    path('profile/change_password',password_change,name='change_password'),
    path('password/',password_change,name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),


]