from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Training
# Create your views here.

class TrainingListView(ListView):
    model = Training

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrainingDetailView(DetailView):
    model = Training

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

