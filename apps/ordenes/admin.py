from django.contrib import admin
from .models import Product_to_order, Order

admin.site.register(Order)
admin.site.register(Product_to_order)