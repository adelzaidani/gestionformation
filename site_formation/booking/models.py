from django.db import models
from training.models import Session
from account.models import Profile

# Create your models here.

class RegistrationSession(models.Model):
    session=models.ForeignKey(Session,verbose_name='Session',on_delete=models.CASCADE)
    student=models.ForeignKey(Profile,verbose_name='Etudiant',on_delete=models.CASCADE,limit_choices_to={'user_type': 1})
    date_of_registration=models.DateTimeField(verbose_name="Date d' inscription",auto_now=True,null=True)

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

    @staticmethod
    def studentRegisterExist(session,student):
        if RegistrationSession.objects.filter(session=session,student=student):
            return True

        return False
        studentRegisterExist=staticmethod(studentRegisterExist)

    """
    Méthode qui permet de savoir le nombre de place déja réservée pour une session determinée.
    """
    def number_seats_booked(self):
        return RegistrationSession.objects.filter(session=self.session).count()


    """
    Méthode qui permet de voir le nombre de place disponible
    pour une session de formation transmise en paramètre.
       
    """

    def available_sites(self, session):
        seats_booked=RegistrationSession.number_seats_booked(session)

        return self.seats_max - seats_booked
