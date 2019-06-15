from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group
from .models import Profile
# Register your models here.

'''
La classe ProfileInline va permettre d'afficher la classe User deja intégrer dans django et la classe Profile que j'ai créer
en une seulle page dans la partie administration.
'''
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
'''
La classe CustomUserAdmin permet de configurer l'affichage des utilisateurs et le choix des champs à afficher. 
'''
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_user_type',)
    list_select_related = ('profile', )

    '''
    La méthode get_user_type permet de recuperer le type d'utilisateur et de l'afficher en String dans la liste.
    '''
    def get_user_type(self,instance):
        type=instance.profile.user_type

        if type == 1 :
            type_string ='Etudiant'
        if type == 2 :
            type_string = 'Formateur'
        if type == 3 :
            type_string = 'Administrateur'


        return type_string

    get_user_type.short_description = "Type d' utilisateur"


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)