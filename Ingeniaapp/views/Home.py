from django.shortcuts import render
from .User import user_required

def Home(request):
    return render(request, 'Inicio/Home.html')
