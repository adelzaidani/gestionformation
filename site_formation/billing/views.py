from django.shortcuts import render,get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse

import pdfkit

from .models import Invoice

'''
print_invoice() permet d'afficher la facture d'une session sous le format pdf
'''
def print_invoice(request,id_session ):
    client = request.user.profile
    invoice = get_object_or_404(Invoice.objects.filter(session=id_session, client=client))
    
    template = get_template('billing/invoice.html')
    html = template.render({'invoice': invoice})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename = facture'+str(invoice.id)+\
                                      '_'+str(invoice.session.training.name)+\
                                      '_'+str(invoice.client.user.last_name)+'.pdf'
    return response


