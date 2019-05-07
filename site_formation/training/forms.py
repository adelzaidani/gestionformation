from django import forms
from .models import Session
from booking.models import RegistrationSession

class ChoiceSessionForm(forms.Form):
    sessions=forms.ModelChoiceField(queryset=Session.objects.all(),empty_label=None)
''''
class RegistrationSessionForm(forms.Form):
    training=forms.CharField(max_length=60,label='Formations')
    date_of_begin=forms.DateField(label='Date de début')
    date_of_end=forms.DateField(label='Date de fin')
    date_of_registration=forms.DateTimeField(label="Date d'inscription")
    price=forms.DecimalField(label='Prix')
    status=forms.CharField(max_length=20, label='Statut')

'''
class RegistrationSessionForm(forms.ModelForm):

    class Meta:
        model=RegistrationSession

        fields=['session','student',
                'status',
                ]