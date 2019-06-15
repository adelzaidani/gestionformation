from django.contrib import admin
from .models import Payment, PaymentSummary
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg, Count,Min,Max
from totalsum.admin import TotalsumAdmin
from django.db.models.functions import Trunc
from django.db.models.fields import DateTimeField



@admin.register(PaymentSummary)
class PaymentSummaryAdmin(admin.ModelAdmin):

    change_list_template = 'admin/payment_summary_change_list.html'
    date_hierarchy = 'date_payment'

    def has_add_permission(self, request):
        return False

    def has_change_permission(request, obj=None):
        return False


    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
            'total_sales': Sum('amount'),
        }

        response.context_data['summary'] = list(
            qs.values('session__training__name').annotate(**metrics).order_by('-total_sales')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )


        return response










class PaymentAdmin(TotalsumAdmin):
    actions = None
    list_display = ['id', 'user', 'date_payment', 'booking','session','stripe_charge_id', 'amount']
    totalsum_list = ['amount']

    unit_of_measure = '&euro;'

    def has_add_permission(self,request):
        return False

    def has_change_permission(self,request, obj=None):
        return False

    def has_delete_permission(self,request, obj=None):
        return False

admin.site.register(Payment,PaymentAdmin)

