from django.shortcuts import render,get_object_or_404
from decimal import Decimal

from .models import Invoice

'''
verifier avant d'afficher la facture que le client dispose bien d'une facture 
pour le numero de session passer en parametre
'''
def print_invoice(request,id_session ):
    client=request.user.profile
    invoice=get_object_or_404(Invoice.objects.filter(session=id_session,client=client))

    return render(request,'billing/invoice.html',{'invoice':invoice})