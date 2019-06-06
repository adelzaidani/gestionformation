from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import  datetime
from booking.models import RegistrationSession
from training.models import Session
from billing.models import Invoice
from .models import Payment
import stripe

stripe.api_key=settings.STRIPE_SECRET_KEY

@login_required(login_url='/account/login/')
def checkout(request):
    publish_key=settings.STRIPE_PUBLIC_KEY
    token = request.POST.get('stripeToken')
    session=Session.objects.get(id=request.session['choice_session'].id)
    student=request.user.profile
    user=request.user
    price=session.training.price
    amount=int(session.training.price * 100)


    if request.method =='POST':

        try:

            charge=stripe.Charge.create(
                    amount=amount,
                    currency="eur",
                    source=token,  # obtained with Stripe.js
            )
            booking = RegistrationSession.objects.create(
                session=session,
                student=student,
                status=2
            )

            if RegistrationSession.available_sites(session) == 0:
                session.full(True)

            payment = Payment.objects.create(
                stripe_charge_id=charge['id'],
                user=user,
                amount=price
            )



            invoice = Invoice.objects.create(
                session=session,
                user=user,
                status=2,
                booking=booking,
                price=price

            )
            messages.success(request, "Votre paiement a été réalisé avec success !")
            return redirect("training:list_training")

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.warning(request, f"{err.get('message')}")
            return redirect("training:list_training")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(request, "Solde insuffisant")
            return redirect("training:list_training")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.warning(request, "Paramètres invalides")
            return redirect("training:list_training")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.warning(request, "Problème d'authentification")
            return redirect("training:list_training")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.warning(request, "Problème de réseau")
            return redirect("training:list_training")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.warning(
                request, "Un problème est survenu, veuillez réessayer plus tard")
            return redirect("training:list_training")

        except Exception as e:
            # send an email to ourselves
            messages.warning(
                request, "Un serieux problème est survenu.")
            return redirect("training:list_training")

    date_today=datetime.now()
    context={'publish_key':publish_key,
             'date_today':date_today}
    template='payment/checkout.html'
    return render(request,template,context)
