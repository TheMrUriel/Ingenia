from django.shortcuts import render
from .User import user_required

def lista_eventos(request):
    return render(request, 'Eventos/lista_eventos.html')
