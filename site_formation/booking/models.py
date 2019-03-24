from django.db import models
from training.models import Session
from account.models import Profile

# Create your models here.

class RegistrationSession(models.Model):
    session=models.ForeignKey(Session,verbose_name='Session',on_delete=models.CASCADE)
    student=models.ForeignKey(Profile,verbose_name='Etudiant',on_delete=models.CASCADE,limit_choices_to={'user_type': 1})
    date_of_registration=models.DateTimeField(verbose_name="Date d' inscription",auto_now=True)

    STATUS = (
            (1, 'En Attente'),
            (2, 'Confirmer'),
        )

    status = models.PositiveSmallIntegerField(verbose_name='Statut',choices=STATUS,default=1)
    class Meta:
        verbose_name="Inscription à une session"
        verbose_name_plural='Inscription aux sessions'

    def __str__(self):
        return self.session.__str__()