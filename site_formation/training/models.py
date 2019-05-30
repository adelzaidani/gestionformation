from django.db import models
# Create your models here.
from account.models import Profile
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill





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
    category=models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='Catégorie')
    number_hours=models.IntegerField(verbose_name='Nombre d''heures')
    image_training = models.ImageField(verbose_name='Image Formation',upload_to='training', blank=True)

    image_thumbnail = ImageSpecField(source='image_training',
                                      processors=[ResizeToFill(700, 400)],
                                      format='JPEG',
                                      options={'quality': 99})



    class Meta:
        verbose_name='Formation'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return self.name

class Session(models.Model):
    date_of_begin=models.DateField(verbose_name='Date de début',null=True)
    date_of_finish=models.DateField(verbose_name='Date de fin',null=True)
    seats_max=models.IntegerField(verbose_name='Nombre de places',null=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Formateur',
                                limit_choices_to={'user_type': 2},default=2)
    full=models.BooleanField(verbose_name='Complet',default=False)







    class Meta:
        verbose_name='Session'
        verbose_name_plural = 'Sessions'







    def __str__(self):
        return 'Du '+ self.date_of_begin.strftime('%d/%m/%Y') + '  au  '\
               + self.date_of_finish.strftime('%d/%m/%Y') + '  '+self.training.__str__()