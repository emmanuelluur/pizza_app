from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/product/<int:id_prod>', login_required(views.add_item_view), name="add_item"),
]