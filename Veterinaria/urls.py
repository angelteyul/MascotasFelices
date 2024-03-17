from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from Veterinaria import views

router = routers.DefaultRouter()
router.register(r'dueno', views.DuenoView, 'dueno')
router.register(r'especie', views.EspecieView, 'especie')
router.register(r'genero', views.GeneroView, 'genero')
router.register(r'raza', views.RazaView, 'raza')
router.register(r'mascota', views.MascotaView, 'mascota')
router.register(r'desparasitante', views.DesparasitanteView, 'desparasitante')
router.register(r'fichadesparacitacion', views.FichaDesparacitacionView, 'fichadesparacitacion')
router.register(r'estado', views.EstadoView, 'estado')
router.register(r'cita', views.CitaView, 'cita')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Veterinaria API'))
]
