from django import template


register = template.Library()

@register.filter(name='percentof')
def percentof(summary_total, total_sales):
    try:
        return "%.2f%%" % ((float(summary_total) / float(total_sales)) * 100)
    except ValueError:
        return ''

