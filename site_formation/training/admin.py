from django.contrib import admin
from booking.models import RegistrationSession

from .models import *

'''
La classe SessionAdmin va permettre de configurer l'affichage des différentes sessions de formation.
'''
class SessionAdmin(admin.ModelAdmin):
    '''
    méthode numer_seats_booked permet de récuperer le nombre de réservation d'une session déterminée.
    '''
    def number_seats_booked(self,instance):

        return RegistrationSession.objects.filter(session=instance.id).count()

    number_seats_booked.short_description = 'Nombre de réservations'

    '''
    Méthode number_seats_available permet de faire le calcul du nombre de place encore disponible pour une session déterminée.
    '''
    def number_seats_available(self,instance):
        max_seats=instance.seats_max
        booked_seats=self.number_seats_booked(instance)
        if max_seats - booked_seats < 0:
            return 0
        return max_seats - booked_seats

    number_seats_available.short_description='nombre de places disponibles'


    list_display = ('training', 'date_of_begin',
                    'date_of_finish','number_seats_booked','number_seats_available')


admin.site.register(Session,SessionAdmin)
admin.site.register(Category)
admin.site.register(Training)