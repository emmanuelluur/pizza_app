from django.shortcuts import render, redirect
from apps.productos.models import Producto
from apps.toppings.models import Topping

# Create your views here.

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
