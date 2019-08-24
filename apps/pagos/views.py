from django.shortcuts import render
from apps.ordenes.models import Order
from django.db.models import Sum

from django.conf import settings
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_view(request, id_order):
    user = request.user
    order = Order.objects.get(id=id_order, is_complete=False)
    total = Order.objects.filter(id=id_order, is_complete=False).aggregate(
        total=Sum('items__total'))
    total_s = Order.objects.filter(id=id_order, is_complete=False).aggregate(
        total=Sum('items__total'))
    template = 'payment.html'
    context = {
        "order": order,
        "total": total,
        "total_s": total_s,
        "user": user,
        "key": settings.STRIPE_PUBLISHABLE_KEY,
    }
    if request.method == "POST":
        amount = int(float(request.POST['mount']) * 100)
        id_order = request.POST['order_id']
        name = request.POST['nameU']
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description=f"Order {id_order} charge customer {name}",
            source=request.POST['stripeToken']
        )
        return render(request, template, {'message': 'Thanks for the pay'})
    return render(request, template, context)
