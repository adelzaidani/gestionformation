from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    date_payment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name

