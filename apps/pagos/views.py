from django.shortcuts import render,redirect
from apps.ordenes.models import Order
from django.db.models import Sum

from django.conf import settings
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_view(request, id_order):
    try:
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
        return render(request, template, context)
    except:
        return redirect('order_view')

    if request.method == "POST":
        id_order = request.POST['order_id']
        update = Order.objects.filter(id=id_order)
        amount = int(float(request.POST['mount']) * 100)
        name = request.POST['nameU']
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description=f"Order {id_order} charge customer {name}",
            source=request.POST['stripeToken']
        )
        # set complete order
        update.update(is_complete=True)
        return render(request, template, {'message': 'Thanks for Purchase'})
    
