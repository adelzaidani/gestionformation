from django.db import models
from django.contrib.auth.models import User
from booking.models import RegistrationSession
from training.models import Session


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(verbose_name='Montant',max_digits=6,decimal_places=2)
    date_payment = models.DateTimeField(verbose_name='Date de paiement',auto_now_add=True)
    booking = models.ForeignKey(RegistrationSession, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Reservation')
    session=models.ForeignKey(Session,on_delete=models.SET_NULL,null=True,blank=True,default=4)
    class Meta:
        verbose_name='Paiement'
        verbose_name_plural='Paiements'

    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name


class PaymentSummary(Payment):
    class Meta:
        proxy = True
        verbose_name = 'Sale Summary'
        verbose_name_plural = 'Sales Summary'