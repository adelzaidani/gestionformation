from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field import formfields
from django.contrib.auth.models import User

class Sign_upForm(UserCreationForm):
    street = forms.CharField(label='Rue',max_length=100, required=True)
    number = forms.IntegerField(label='Numéro',required=True, max_value=9999)
    postal_code = forms.IntegerField(label='Code Postal',max_value=9999, required=True)
    locality = forms.CharField(label= 'Localité',max_length=150, required=True)
    phone = formfields.PhoneNumberField(label='Téléphone',required=True)
    place_of_birth = forms.CharField(label='Lieu de naissance',max_length=150, required=True)
    birth_date = forms.DateField(label='Date de naissance',required=True)
    degree = forms.CharField(label='Diplôme',max_length=150, required=False)


    class Meta:
        model = User
        fields = ('last_name','first_name','username', 'email','street',
                  'number','postal_code','locality','phone',
                  'place_of_birth','birth_date',
                  'degree','password1', 'password2',)


