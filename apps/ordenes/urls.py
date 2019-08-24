from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/product/<int:id_prod>', login_required(views.add_item_view), name="add_item"),
    path('add/product/', login_required(views.add_item_post), name="add_item_post"),
    path('cart/', login_required(views.cart_view), name="cart_view"),
    path('success/', login_required(views.success_add), name="success_add"),
    path('item/delete/<int:id_prod>', login_required(views.delete_item), name="delete_item"),
]