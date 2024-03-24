from django.contrib import admin
from django.urls import path
from .views.views import *

app_name = "Ingeiaapp"

urlpatterns = [
    # Inicio
    path('', Home, name='home'),
    path('home/', Home, name='home'),

    # Usuario
    path('register/', register, name='usuario_register'),
    path('login/', my_login, name='usuario_login'),
    path('logout/', user_logout, name="user-logout"),
]
