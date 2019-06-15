from django.db import models
from django.db.models.signals import post_save
from account.models import Profile
from training.models import Session
from booking.models import RegistrationSession
from django.dispatch import receiver
from datetime import date, datetime, timedelta

class Attendance(models.Model):
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    date_of_attendance=models.DateField(verbose_name="Date de présence")
    ATTENDANCE_CHOICES = (
        (1, 'Présent'),
        (2, 'Absent'),
        (3, 'Absence justifiée'),
        (4, 'Absence non justifiée'),
    )

    attendance_choices = models.PositiveSmallIntegerField(choices=ATTENDANCE_CHOICES, default=2, verbose_name='Présence')
    student= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Etudiant',
                                limit_choices_to={'user_type': 1}, default=1)

    class Meta:
        verbose_name='Présence'
        verbose_name_plural='Présences'

    def __str__(self):
        return self.session.__str__() +'--' +str(self.date_of_attendance)


class Assessment(models.Model):
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Etudiant',
                                limit_choices_to={'user_type': 1}, default=1)
    assessment=models.PositiveSmallIntegerField(default=0,verbose_name='Evaluation')

    class Meta:
        verbose_name='Evaluations'
        verbose_name_plural='Evaluation'