from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

#Création du model Profil

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    street=models.CharField(max_length=100)
    number=models.IntegerField(null=True)
    postal_code=models.IntegerField(null=True)
    locality=models.CharField(max_length=150)
    phone=PhoneNumberField()
    place_of_birth=models.CharField(max_length=150)
    birth_date=models.DateField(null=True)
    degree=models.CharField(max_length=150)
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()