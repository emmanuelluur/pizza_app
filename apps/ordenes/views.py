from django.shortcuts import render, redirect
from apps.productos.models import Producto
from apps.toppings.models import Topping
from django.http import HttpResponse, JsonResponse

from apps.productos.models import Producto
from django.contrib.auth.models import User
from .models import Product_to_order

import datetime
# Create your views here.


def cart_view(request):
    current_user = request.user
    products = Product_to_order.objects.all().filter(user=current_user.id, is_ordered=False)
    total = 0
    if len(products) > 0:
        for item in products:
            total += item.total
    context = {
        'total': total,
        'products': products
    }
    template = "cart_items.html"
    return render(request, template, context)

def add_item_view(request, id_prod):
    """ vista agrega producto a carro """
    template = "product_add.html"
    product = Producto.objects.get(id=id_prod)
    toppings = Topping.objects.all()
    context = {
        'product': product,
        'toppings': toppings,
    }

    return render(request, template, context)


def add_item_post(request):
    if request.method == "POST":
        id_user = request.POST['user']
        id_prod = request.POST['product']
        user = User.objects.get(id=id_user)
        product = Producto.objects.get(id=id_prod)

        item = Product_to_order.objects.create(user=user,
                                               product=product,
                                               quantity = request.POST['quantity'],
                                               price= request.POST['price'],
                                               toppings=request.POST['toppings'],
                                               total_toppings=request.POST['total_toppings'],
                                               total=request.POST['total'],
                                               date_added=datetime.datetime.now(),
                                               )
        item.save()
        return JsonResponse({"message": "Product added"})

    return HttpResponse("No")

def success_add(request):
    template = "success_add.html"
    return render(request, template)
