from django.db import models
from apps.productos.models import Producto
from django.contrib.auth.models import User


class Product_to_order(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    toppings = models.TextField(blank=True,null=True)
    total_toppings = models.FloatField(null=True)
    total = models.FloatField()
    is_ordered = models.BooleanField(default=False, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(auto_now=False, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Product_to_order, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.user.first_name
