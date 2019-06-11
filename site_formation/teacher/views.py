from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from training.models import Session
from booking.models import RegistrationSession
from teacher.models import Attendance, Assessment
from account.models import Profile
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login/')
def session_teacher(request):
    teacher=request.user.profile
    session_teacher=get_list_or_404(Session.objects.filter(teacher=teacher))
    return render(request,'teacher/my_courses_teacher.html',{'session_teacher':session_teacher})

@login_required(login_url='/account/login/')
def training_student(request,id_session):
    teacher = request.user.profile
    test_session = get_object_or_404(Session.objects.filter(teacher=teacher, id=id_session))
    registrations = get_list_or_404(RegistrationSession.objects.filter(session=id_session, status=2))
    return render(request,'teacher/list_students.html',{'registrations':registrations})

@login_required(login_url='/account/login/')
def list_attendance(request,id_session):
    teacher=request.user.profile
    session = get_object_or_404(Session.objects.filter(teacher=teacher, id=id_session))

    if Attendance.objects.filter(session=session,date_of_attendance=session.date_of_begin).exists():
        attendances = get_list_or_404(Attendance.objects.filter(session=id_session,
                                                                date_of_attendance=session.date_of_begin))
    else:
        attendances=get_list_or_404(RegistrationSession.objects.filter(session=session,status=2))
    return render(request,'teacher/list_attendance.html',{'attendances':attendances,'session':session})

@csrf_exempt
@login_required(login_url='/account/login/')
def list_attendance_date_change(request):

    if request.is_ajax():
        date_selected=request.POST['date_selected']
        id_session=request.POST['session']
        session=get_object_or_404(Session.objects.filter(id=id_session))

        if Attendance.objects.filter(session=session,date_of_attendance=date_selected).exists():
            attendances=get_list_or_404(Attendance.objects.filter(session=session,date_of_attendance=date_selected))
            list=[]
            for attendance in attendances:
                list.append({
                    'id_student':attendance.student.user.id,
                    'last_name':attendance.student.user.last_name,
                    'first_name':attendance.student.user.first_name,
                    'birth_date':attendance.student.birth_date,
                    'attendance':attendance.attendance_choices
                })


        else:
            attendances=get_list_or_404(RegistrationSession.objects.filter(session=session,status=2))
            list=[]
            for attendance in attendances:
                list.append({

                    'id_student': attendance.student.user.id,
                    'last_name': attendance.student.user.last_name,
                    'first_name': attendance.student.user.first_name,
                    'birth_date': attendance.student.birth_date,
                    'attendance': 2
                })


    print(list)
    return JsonResponse(list,safe=False)



@login_required(login_url='/account/login/')
def list_assessment(request,id_session):
    teacher=request.user.profile
    session = get_object_or_404(Session.objects.filter(teacher=teacher, id=id_session))


    if Assessment.objects.filter(session=session).exists():
        assessments=get_list_or_404(Assessment.objects.filter(session=session))
    else:
        assessments=get_list_or_404(RegistrationSession.objects.filter(session=session,status=2))
    return render(request,'teacher/list_assessment.html',{'assessments':assessments,'session':session})

@csrf_exempt
@login_required(login_url='/account/login/')
def save_attendance(request):

    data = {
        'exist': False,
        'message':'Les présences ont été réalisées avec succès !'
    }

    post=request.POST['pTableData']
    list_attendance=json.loads(post)
    date=list_attendance[0]['date']
    fdate=datetime.strptime(date, "%Y-%m-%d").date()
    id_session=list_attendance[0]['session']
    session=Session.objects.get(id=id_session)
    if Attendance.objects.filter(session=id_session,date_of_attendance=date).exists():
        data['exist']=True
        data['message']='les présences ont déja été réalisées pour le ' \
                        + list_attendance[0]['date'] + "Veuillez contacter l'administrateur " \
                                                       "pour une modification."

    elif    fdate < session.date_of_begin or fdate > session.date_of_finish:

            data['exist'] = True
            data['message'] = 'La date doit être comprise entre le début et la fin de la session.'

    else:

        for attendance in list_attendance:
            student=Profile.objects.get(user_id=attendance['id_client'],user_type=1)
            attendance_value=attendance['attendance']

            Attendance.objects.create(session=session,
                                      date_of_attendance=date,
                                      attendance_choices=attendance_value,
                                      student=student)
    return JsonResponse(data)

@csrf_exempt
@login_required(login_url='/account/login/')
def save_assessment(request):

    data={
        'exist':False,
        'message':'Les notes ont été enregistrées avec succès !'
    }

    post = request.POST['tableAssessment']
    list_assessment = json.loads(post)
    id_session=list_assessment[0]['session']
    session=Session.objects.get(id=id_session)

    if Assessment.objects.filter(session=session).exists():

        for assessment in list_assessment:
            student=Profile.objects.get(user_id=assessment['id_client'],user_type=1)
            assessment_value=assessment['assessment']
            Assessment.objects.filter(session=session, student=student).update(assessment=assessment_value)


            data['exist']=True,
            data['message']= 'Les notes ont été modifiées avec succès !'


    else:
        for assessment in list_assessment:
            student=Profile.objects.get(user_id=assessment['id_client'],user_type=1)
            assessment_value=assessment['assessment']
            Assessment.objects.create(session=session, student=student,assessment=assessment_value)





    return JsonResponse(data)