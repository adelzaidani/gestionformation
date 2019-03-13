from django.db import models
# Create your models here.
from account.models import Profile





class Category(models.Model):
    name=models.CharField(verbose_name='nom de la catégorie',max_length=150)

    class Meta:
        verbose_name='Categorie'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name



class Training(models.Model):
    name=models.CharField(verbose_name='Nom de la formation', max_length=150)
    description=models.TextField(verbose_name='Description')
    price=models.DecimalField(verbose_name='Prix',max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    number_hours=models.IntegerField(verbose_name='Nombre d''heures')
    teacher=models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='Formateur',
                              limit_choices_to={'user_type': 2})


    class Meta:
        verbose_name='Formation'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return self.name

class Session(models.Model):
    date_of_begin=models.DateField(verbose_name='Date de début',null=True)
    date_of_finish=models.DateField(verbose_name='Date de fin',null=True)
    places_max=models.IntegerField(verbose_name='Nombre de places',null=True)
    availabe_places=models.IntegerField(verbose_name='Nombre de places restantes',null=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    full=models.BooleanField(verbose_name='Complet',default=False)



    class Meta:
        verbose_name='Session'
        verbose_name_plural = 'Sessions'

    def get_available_places(self):
        return self.availabe_places

    def is_full(self):
        return self.full



    def __str__(self):
        return 'Du '+ self.date_of_begin.strftime('%d/%m/%Y') + '  au  '\
               + self.date_of_finish.strftime('%d/%m/%Y') + '  '+self.training.__str__()