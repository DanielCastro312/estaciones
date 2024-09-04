from django.shortcuts import render
from .models import Estacion

def ver_estaciones(request):
    estaciones = Estacion.objects.all()
    return render(request, 'estaciones/ver_estaciones.html', {'estaciones': estaciones})
