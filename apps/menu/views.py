from django.shortcuts import render
from apps.productos.models import Producto
from apps.categorias.models import Categoria
# Create your views here.

def menu(request):
	"""Categories query"""
	categoria_pizza = Categoria.objects.get(name='pizza')
	categoria_salad = Categoria.objects.get(name='salad')
	categoria_sub = Categoria.objects.get(name='sub')
	"""Products query"""
	pizza = Producto.objects.all().filter(category=categoria_pizza)
	salads = Producto.objects.all().filter(category=categoria_salad)
	subs = Producto.objects.all().filter(category=categoria_sub)
	# Context
	context = {
	'pizza': pizza,
	'salads': salads,
	'subs': subs,
	}
	# view
	return render(request, './menu.html', context)