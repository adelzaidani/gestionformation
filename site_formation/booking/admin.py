from django.contrib import admin
from .models import RegistrationSession

# Register your models here.
class RegistrationSessionAdmin(admin.ModelAdmin):
       list_display = ('id','student','session','date_of_registration','status')

       fields = ('id',
                 'session',
                 'student',
                 'date_of_registration',
                 'status',
                 )
       readonly_fields = ['date_of_registration']

       list_filter = ('date_of_registration','session','status')






admin.site.register(RegistrationSession,RegistrationSessionAdmin)