from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('view/<int:id_order>/', login_required(views.payment_view), name="payment_view")
]