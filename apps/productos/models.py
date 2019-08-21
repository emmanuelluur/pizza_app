from django.db import models
from apps.categorias.models import Categoria
# Create your models here.


class Producto(models.Model):
    name = models.CharField(max_length=60)
    image_url = models.URLField(max_length=200, blank=True)
    has_topping = models.BooleanField(blank=True, null=True)
    has_extra = models.BooleanField(blank=True, null=True)
    small_price = models.FloatField(blank=True,null=True)
    large_price = models.FloatField(blank=True,null=True)
    category = models.ForeignKey(
        Categoria, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
