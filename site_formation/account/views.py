from django.shortcuts import render, redirect
from .forms import Sign_upForm, EditUserForm,EditProfileForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required



def sign_up(request):

    if request.method == 'POST':
        form = Sign_upForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # chargement de l'instance profile qui est crée par le signal.
            user.profile.street = form.cleaned_data.get('street')
            user.profile.number = form.cleaned_data.get('number')
            user.profile.postal_code = form.cleaned_data.get('postal_code')
            user.profile.locality = form.cleaned_data.get('locality')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.place_of_birth = form.cleaned_data.get('place_of_birth')
            user.profile.degree = form.cleaned_data.get('degree')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'l\'inscription a été effectuée avec succès.')
            return redirect('home:home')
    else:
        form = Sign_upForm()

    return render(request,'account/sign_up.html',{'form':form})



@login_required(login_url='/account/login/')
@transaction.atomic
def editProfile(request):
    if request.method == 'POST':
        form_user=EditUserForm(request.POST,request.FILES,instance=request.user)
        form_profile = EditProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request,'Votre profil a été mise à jour avec succès ')
            return render(request,'account/edit_profile.html',{'form_user':form_user, 'form_profile':form_profile})
        else:
            messages.error(request,'Veuillez corriger les erreurs svp ! ')

    else:
        form_user = EditUserForm(instance=request.user)
        form_profile=EditProfileForm(instance=request.user.profile)
    return render(request,'account/edit_profile.html',{'form_user':form_user, 'form_profile':form_profile})

@login_required(login_url='/account/login/')
def password_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('edit_profile')
        else:

            return redirect('change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        return render(request,'account/change_password.html',{'form':form})
