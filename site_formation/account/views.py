from django.shortcuts import render, redirect
from .forms import Sign_upForm
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Profile

def home(request):
    return render(request,'home.html')


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
            user.profile.is_student=True
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Sign_upForm()

    return render(request,'account/sign_up.html',{'form':form})

class ProfileUpdate(UpdateView):

    fields = '__all__'

    model = Profile
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user.profile



class MyProfile(DetailView):


    template_name = 'account/my_profile.html'


    def get_object(self):
        return self.request.user.profile
