from django.urls import path
from . import views

app_name='training'

urlpatterns = [

    path('',views.TrainingListView.as_view(),name='list_training'),
    path('<int:id>/',views.training_detail,name='detail_training'),
    path('my_training/',views.my_training,name='my_training'),
]
