from django.shortcuts import render
from training.models import Training
from account.models import Profile

# Create your views here.


def home(request):
    trainings=Training.objects.all()
    teachers=Profile.objects.filter(user_type=2)
    return render(request,'home/home.html',{'trainings':trainings, 'teachers':teachers})