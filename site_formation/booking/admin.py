from django.contrib import admin
from .models import RegistrationSession

# Register your models here.
class RegistrationSessionAdmin(admin.ModelAdmin):
       list_display =('session','student',)

       fields = ('session',
                 'student',
                 'date_of_registration',
                 'status',
                 )
       readonly_fields = ['date_of_registration']


admin.site.register(RegistrationSession,RegistrationSessionAdmin)