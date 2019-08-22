from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name="login_auth"),
    path('signin/', views.register_user, name="signin"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
