from django import forms
from .models import Session
from booking.models import RegistrationSession

class ChoiceSessionForm(forms.Form):
    sessions=forms.ModelChoiceField(queryset=Session.objects.all(),empty_label=None)
