from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from phonenumber_field import formfields
from django.contrib.auth.models import User
from .models import Profile
from bootstrap_datepicker_plus import DatePickerInput

class Sign_upForm(UserCreationForm):
    street = forms.CharField(label='',max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Rue'}))
    number = forms.IntegerField(label='',required=True, max_value=9999,widget=forms.TextInput(attrs={'placeholder': 'Numero'}))
    postal_code = forms.IntegerField(label='',max_value=9999, required=True,widget=forms.TextInput(attrs={'placeholder': 'Code Postal'}))
    locality = forms.CharField(label= '',max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Localité'}))
    phone = formfields.PhoneNumberField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}))
    place_of_birth = forms.CharField(label='',max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Lieu de naissance'}))
    birth_date = forms.DateField(input_formats=['%d/%m/%Y'],label='',required=True, widget=forms.TextInput(attrs={'class':'datepicker','placeholder': 'Date de naissance'}))
    degree = forms.CharField(label='',max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Diplôme'}))


    class Meta:
        model = User
        fields = ('last_name','first_name','username', 'email','street',
                  'number','postal_code','locality','phone',
                  'place_of_birth','birth_date',
                  'degree','password1', 'password2',)


        labels={
            'last_name':'',
            'first_name':'',
            'username':'',
            'email':'',
        }

        widgets={
            'last_name':forms.fields.TextInput(attrs={'placeholder':'Nom'}),
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'Prénom'}),
            'username': forms.fields.TextInput(attrs={'placeholder': 'Nom d \'utilisateur'}),
            'email':forms.fields.TextInput(attrs={'placeholder': 'Email'}),
            'password1': forms.fields.TextInput(attrs={'placeholder': 'Mot de passe'}),
            'password2': forms.fields.TextInput(attrs={'placeholder': 'Confirmer mot de passe'}),

        }

    def __init__(self, *args, **kwargs):
        super(Sign_upForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].label=''
            self.fields[fieldname].help_text=None

        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe'})

class EditUserForm(UserChangeForm):

   class Meta:

        model=User

        fields=('last_name','first_name','username', 'email','password')



class EditProfileForm(ModelForm):

    street = forms.CharField(label='Rue', max_length=100, required=True)
    number = forms.IntegerField(label='Numéro', required=True, max_value=9999)
    postal_code = forms.IntegerField(label='Code Postal', max_value=9999, required=True)
    locality = forms.CharField(label='Localité', max_length=150, required=True)
    phone = formfields.PhoneNumberField(label='Téléphone', required=True)
    place_of_birth = forms.CharField(label='Lieu de naissance', max_length=150, required=True)
    birth_date = forms.DateField(label='Date de naissance', required=True)
    degree = forms.CharField(label='Diplôme', max_length=150, required=False)

    class Meta:
        model= Profile

        fields=('street','number','postal_code','locality','phone',
                  'place_of_birth','birth_date',
                  'degree')
