from django.contrib import admin
from .models import ProductOrder, ToppingOrder, Order
# Register your models here.

admin.site.register(ProductOrder)
admin.site.register(ToppingOrder)
admin.site.register(Order)