from django.db import models
from training.models import Session
from account.models import Profile
from booking.models import RegistrationSession

# Create your models here.
class Invoice(models.Model):
    session=models.ForeignKey(Session,on_delete=models.CASCADE,verbose_name='Session')
    date=models.DateField(verbose_name='Date de facturation', null=True, auto_now=True)
    client=models.ForeignKey(Profile,verbose_name='Etudiant',on_delete=models.CASCADE,limit_choices_to={'user_type': 1})
    STATUS = (
        (1, 'Payable'),
        (2, 'Payer'),
        (3, 'Annuler'),
    )

    status = models.PositiveSmallIntegerField(verbose_name='Statut', choices=STATUS, default=1)
    booking=models.ForeignKey(RegistrationSession, on_delete=models.CASCADE, verbose_name='Reservation')