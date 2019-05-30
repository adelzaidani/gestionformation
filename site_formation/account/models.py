from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save


#Création du model Profil

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    street=models.CharField(verbose_name='Rue',max_length=100)
    number=models.IntegerField(verbose_name='Numéro',null=True)
    postal_code=models.IntegerField(verbose_name='Code Postal',null=True)
    locality=models.CharField(verbose_name='Localité',max_length=150)
    phone=PhoneNumberField(verbose_name='Télephone')
    place_of_birth=models.CharField(verbose_name='Lieu de naissance',max_length=150)
    birth_date=models.DateField(verbose_name='Date de naissance',null=True)
    degree=models.CharField(verbose_name='Diplome',max_length=150)
    image_profile=models.ImageField(upload_to='account',blank=True)
    USER_TYPE_CHOICES = (
        (1, 'Etudiant'),
        (2, 'Formateur'),
        (3, 'Administrateur'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1, verbose_name='Type')

    def __str__(self):
        return self.user.last_name +'  '+self.user.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


