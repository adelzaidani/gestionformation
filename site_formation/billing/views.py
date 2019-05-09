from django.shortcuts import render
from .models import Invoice


def print_invoice(request,session_id):
    client=request.user
    invoice=Invoice.Objects.filter(session=session_id,client=client)

    return render(request,'billing/invoice.html',{'invoice':invoice})