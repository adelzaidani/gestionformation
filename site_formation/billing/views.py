from django.shortcuts import render,get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pdfkit

from .models import Invoice

'''
print_invoice() permet d'afficher la facture d'une session sous le format pdf
utilisation de la librairie pdfkit.
'''
@login_required(login_url='/account/login/')
def print_invoice(request,id_session ):
    user_invoice = request.user
    invoice = get_object_or_404(Invoice.objects.filter(session=id_session, user=user_invoice))
    
    template = get_template('billing/invoice.html')
    html = template.render({'invoice': invoice})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename = facture'+str(invoice.id)+\
                                      '_'+str(invoice.session.id)+\
                                      '_'+str(invoice.user.id)+'.pdf'
    return response


