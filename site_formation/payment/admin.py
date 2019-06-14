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
            qs
                .values('session')
                .annotate(**metrics)
                .order_by('-total_sales')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        period = get_next_in_date_hierarchy(
            request, self.date_hierarchy)

        response.context_data['period'] = period

        summary_over_time = qs.annotate(
            period=Trunc(
                'date_payment',
                period,
                output_field=DateTimeField(),
            ),
        ).values('period') \
            .annotate(total=Sum('amount')) \
            .order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
                ((x['total'] or 0) - low) / (high - low) * 100
                if high > low else 0,
        } for x in summary_over_time]

        return response

def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'

    if date_hierarchy + '__month' in request.GET:
        return 'day'

    if date_hierarchy + '__year' in request.GET:
        return 'week'

    return 'month'









class PaymentAdmin(TotalsumAdmin):
    list_display = ['id', 'user', 'date_payment', 'booking','session','stripe_charge_id', 'amount']
    totalsum_list = ['amount']

    unit_of_measure = '&euro;'



admin.site.register(Payment,PaymentAdmin)

