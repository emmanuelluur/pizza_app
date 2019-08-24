from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/product/<int:id_prod>', login_required(views.add_item_view), name="add_item"), #form add 
    path('add/product/', login_required(views.add_item_post), name="add_item_post"), # method post
    path('cart/', login_required(views.cart_view), name="cart_view"), # view cart
    path('success/', login_required(views.success_add), name="success_add"), # view for succes item added
    path('item/delete/<int:id_prod>', login_required(views.delete_item), name="delete_item"),
    path('create/', login_required(views.order_create), name='create_order'), # create order
    path('', login_required(views.order_view), name='order_view'), # orders info
]