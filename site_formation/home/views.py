from django.shortcuts import render
from training.models import Training

# Create your views here.


def home(request):
    trainings=Training.objects.all()
    return render(request,'index.html',{'trainings':trainings})