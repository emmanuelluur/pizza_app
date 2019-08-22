from django.db import models
from apps.productos.models import Producto
from apps.toppings.models import Topping
from django.contrib.auth.models import User


# Create your models here.

class ProductOrder(models.Model):
    product = models.OneToOneField(
        Producto, on_delete=models.CASCADE, null=True)
    is_order = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class ToppingOrder(models.Model):
    topping = models.OneToOneField(
        Topping, on_delete=models.CASCADE, null=True)
    is_order = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topping.name


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_order = models.BooleanField(default=False)
    items = models.ManyToManyField(ProductOrder)
    toppings = models.ManyToManyField(ToppingOrder)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.name
