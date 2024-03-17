from rest_framework import serializers
from .models import Dueno, Especie, Genero, Raza, Mascota, Desparasitante, FichaDesparasitacion, Estado, Cita

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'


class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class DesparasitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desparasitante
        fields = '__all__'


class FichaDesparasitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaDesparasitacion
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
