from django.db import models
from django.contrib.auth.models import User
from training.models import Session
from account.models import Profile
from booking.models import RegistrationSession

# Create your models here.
class Invoice(models.Model):
    session=models.ForeignKey(Session,on_delete=models.SET_NULL,verbose_name='Session',null=True, blank=True)
    date=models.DateField(verbose_name='Date de facturation', null=True, auto_now=True)
    user=models.ForeignKey(User,verbose_name='Client',on_delete=models.SET_NULL,null=True, blank=True)
    STATUS = (
        (1, 'Payable'),
        (2, 'Payer'),
        (3, 'Annuler'),
    )

    status = models.PositiveSmallIntegerField(verbose_name='Statut', choices=STATUS, default=1)
    booking=models.ForeignKey(RegistrationSession, on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Reservation')
    price=models.DecimalField(verbose_name='Prix',max_digits=6,decimal_places=2)