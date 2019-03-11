from django.urls import path
from . import views

app_name='training'

urlpatterns = [

    path('liste_training',views.TrainingListView.as_view(template_name='training/list_training.html'),
         name='list_training'),
    path('<slug:slug>/',views.TrainingDetailView.as_view(template_name='training/detail_trainig.html'),
        name='detail_training'),
]
