from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

from .models import Dueno, Especie, Genero, Raza, Mascota, Desparasitante, FichaDesparasitacion, Estado, Cita
from .serializer import DuenoSerializer, EspecieSerializer, GeneroSerializer, RazaSerializer, MascotaSerializer, DesparasitanteSerializer, FichaDesparasitacionSerializer, EstadoSerializer, CitaSerializer

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is None or not user.check_password(password):
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)})


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
