from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id','user','date','status','booking','price','session']
    list_filter = ['date','status','session']
    def has_add_permission(self, request,obj=None):
        return False

    def has_change_permission(self,request, obj=None):
        return False

    def has_delete_permission(self,request, obj=None):
        return False

admin.site.register(Invoice,InvoiceAdmin)