from django.urls import path
from . import views

urlpatterns = [
    path('verEstaciones/', views.ver_estaciones, name='ver_estaciones'),  # Ruta para ver estaciones
]
