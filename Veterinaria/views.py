from rest_framework import viewsets
from .models import Dueno, Especie, Genero, Raza, Mascota, Desparasitante, FichaDesparasitacion, Estado, Cita
from .serializer import DuenoSerializer, EspecieSerializer, GeneroSerializer, RazaSerializer, MascotaSerializer, DesparasitanteSerializer, FichaDesparasitacionSerializer, EstadoSerializer, CitaSerializer

# Create your views here.

class DuenoView(viewsets.ModelViewSet):
    serializer_class = DuenoSerializer
    queryset = Dueno.objects.all()


class EspecieView(viewsets.ModelViewSet):
    serializer_class = EspecieSerializer
    queryset = Especie.objects.all()


class GeneroView(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()


class RazaView(viewsets.ModelViewSet):
    serializer_class = RazaSerializer
    queryset = Raza.objects.all()


class MascotaView(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()


class DesparasitanteView(viewsets.ModelViewSet):
    serializer_class = DesparasitanteSerializer
    queryset = Desparasitante.objects.all()


class FichaDesparacitacionView(viewsets.ModelViewSet):
    serializer_class = FichaDesparasitacionSerializer
    queryset = FichaDesparasitacion.objects.all()


class EstadoView(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()


class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
