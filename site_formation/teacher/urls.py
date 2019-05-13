from django.urls import path
from . import views

app_name='teacher'

urlpatterns =[
    path('my_courses_teacher/', views.session_teacher, name='courses_teacher'),

]