from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Training, Session
from django.shortcuts import get_object_or_404
# Create your views here.





class TrainingListView(ListView):

    model = Training
    template_name = 'training/training_list.html'
    queryset = Training.objects.all()


def training_detail(request,id):
    training=get_object_or_404(Training,id=id)
    sessions=Session.objects.filter(training=id,full=False)
    context={'training':training,'sessions':sessions}
    return render(request,'training/training_detail.html',context)

