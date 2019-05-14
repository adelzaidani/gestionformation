from django.urls import path
from . import views

app_name='teacher'

urlpatterns =[
    path('my_courses_teacher/', views.session_teacher, name='courses_teacher'),
    path('training_student/<int:id_session>',views.training_student,name='training_student'),
    path('list_attendance/',views.list_attendance, name='list_attendance'),


]