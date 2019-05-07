from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Training, Session
from django.shortcuts import get_object_or_404
from .forms import ChoiceSessionForm
from booking.models import RegistrationSession
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



# Create your views here.





class TrainingListView(ListView):

    model = Training
    template_name = 'training/training_list.html'
    queryset = Training.objects.all()


def training_detail(request,id):
    training=get_object_or_404(Training,id=id)

    if request.method=='POST':
        form_session=ChoiceSessionForm(request.POST)
        form_session.fields['sessions'].queryset = Session.objects.filter(training=id, full=False)

        if form_session.is_valid() and request.user.is_authenticated:
            session=form_session.cleaned_data['sessions']
            student=Profile.objects.get(user=request.user)
            if  not RegistrationSession.studentRegisterExist(session,student):
                registration_session=RegistrationSession.objects.create(session=session,student=student)

                return redirect('training:list_training')


    else:

        form_session=ChoiceSessionForm()
        form_session.fields['sessions'].queryset = Session.objects.filter(training=id, full=False)


    context={'training':training,
             'form_session':form_session,
             }




    return render(request,'training/training_detail.html',context)

'''
La vue my_training va permettre d'afficher l'ensemble des réservations de formations pour
un utilisateur déterminé.
'''
def my_training(request):

    current_user=request.user.profile
    booking_user=RegistrationSession.objects.filter(student=current_user).exclude(status=3)
    return render(request,'training/my_training.html',{'booking_user':booking_user})

'''
La vue update_registration permet d'annuler une inscription elle prend 
comme paramètre request et l'id de l'inscription.
'''
def update_registration(request,id_registration):

    if request.method== 'POST':
        try:
            registration = RegistrationSession.objects.get(id=id_registration, student=request.user.profile)
            registration.status=3
            registration.save()
        except ObjectDoesNotExist():
            messages.ERROR(request,"Votre formation n'a pas pu être annuler .")
            return redirect('training:my_training')

        messages.success(request, 'Votre inscription à bien été annuler .')
        return redirect('training:my_training')



    return redirect('training:my_training')