from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from phonenumber_field import formfields
from django.contrib.auth.models import User
from .models import Profile



class Sign_upForm(UserCreationForm):
    last_name = forms.CharField(label='Nom', required=True, widget=forms.fields.TextInput(
        attrs={
            'placeholder': 'Nom',
            'class': 'form-control'
    }))

    first_name = forms.CharField(label='Prénom', required=True, widget=forms.fields.TextInput(
        attrs={
            'placeholder': 'Prénom',
            'class': 'form-control'
    }))


    email=forms.EmailField(label='Adresse électronique', required=True,widget=forms.EmailInput(
        attrs={
        'placeholder':'Adresse éléctronique',
        'class': 'form-control'
    }))
    street = forms.CharField(label='Rue',max_length=100, required=True,widget=forms.TextInput(
        attrs={
        'placeholder': 'Rue',
        'class': 'form-control'
    }))
    number = forms.IntegerField(label='N°',required=True, max_value=9999,widget=forms.NumberInput(
        attrs={
        'placeholder': 'Numero',
        'class': 'form-control'
    }))
    postal_code = forms.IntegerField(label='Code postal',max_value=9999, required=True,widget=forms.NumberInput(
        attrs={
        'placeholder': 'Code Postal',
        'class': 'form-control'
    }))
    locality = forms.CharField(label= 'Localité',max_length=150, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Localité',
               'class':'form-control'
        }))
    phone = formfields.PhoneNumberField(label='Téléphone',required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Téléphone (+32123456789)',
               'class': 'form-control'
        }))
    place_of_birth = forms.CharField(label='Lieu de naissance',max_length=150, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Lieu de naissance',
               'class': 'form-control'
        }))
    birth_date = forms.DateField(input_formats=['%d/%m/%Y'],label='Date de naissance',required=True, widget=forms.DateInput(
        attrs={'class':'form-control',
               'placeholder': 'Date de naissance (01/01/1980)'
        }))
    degree = forms.CharField(label='Diplôme',max_length=150, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Diplôme',
               'class': 'form-control'
        }))


    class Meta:
        model = User

        fields = ('last_name','first_name','username', 'email','street',
                  'number','postal_code','locality','phone',
                  'place_of_birth','birth_date',
                  'degree','password1', 'password2',)




        widgets={
            'username': forms.fields.TextInput(attrs={'placeholder': 'Nom d \'utilisateur','class':'form-control'}),
            'email':forms.fields.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}),
            'password1': forms.fields.TextInput(attrs={'placeholder': 'Mot de passe', 'class':'form-control'}),
            'password2': forms.fields.TextInput(attrs={'placeholder': 'Confirmer mot de passe','class':'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(Sign_upForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2', 'username']:
            self.fields[fieldname].help_text = None

        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Mot de passe','class':'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe','class':'form-control'})



class EditUserForm(ModelForm):

   class Meta:

        model=User

        fields=('last_name','first_name', 'email','username')

        labels = {
               'last_name': 'Nom',
               'first_name': 'Prenom',
               'email': 'Adresse électronique',
               'username': 'Nom d\'utilisateur',
        }

        widgets = {
           'last_name': forms.fields.TextInput(attrs={'placeholder': 'Nom',
                                                      'class':'form-control'}),
           'first_name': forms.fields.TextInput(attrs={'placeholder': 'Prénom',
                                                       'class':'form-control'}),
           'username': forms.fields.TextInput(attrs={'placeholder': 'Nom d \'utilisateur',
                                                     'class':'form-control'}),
           'email': forms.fields.TextInput(attrs={'placeholder': 'Email',
                                                  'class':'form-control'}),


        }




class EditProfileForm(ModelForm):

    street = forms.CharField(label='Rue',required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',

        }
    ))
    number = forms.IntegerField(label='Numéro', required=True, max_value=9999, widget=forms.NumberInput(
        attrs={
            'class':'form-control',

        }

    ))
    postal_code = forms.IntegerField(label='Code Postal', max_value=9999, required=True,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
        }
    ))
    locality = forms.CharField(label='Localité', max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    phone = formfields.PhoneNumberField(label='Téléphone', required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    place_of_birth = forms.CharField(label='Lieu de naissance', max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }


    ))
    birth_date = forms.DateField(label='Date de naissance', required=True,widget=forms.DateInput(
        attrs={
            'class':'form-control',
        }


    ))
    degree = forms.CharField(label='Diplôme', max_length=150, required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }


    ))

    image_profile=forms.ImageField(label='Photo du profil',required=False)


    class Meta:
        model= Profile

        fields=('street','number','postal_code','locality','phone',
                  'place_of_birth','birth_date',
                  'degree','image_profile')
