from django.contrib import admin
from .models import Payment
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg
from totalsum.admin import TotalsumAdmin







class PaymentAdmin(TotalsumAdmin):
    list_display = ['id', 'user', 'date_payment', 'booking', 'stripe_charge_id', 'amount']
    totalsum_list = ['amount']
    unit_of_measure = '&euro;'


admin.site.register(Payment,PaymentAdmin)

