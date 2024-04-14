from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from Veterinaria import views

router = routers.DefaultRouter()

router.register(r'duenos', views.DuenoView, 'dueno')
router.register(r'especies', views.EspecieView, 'especie')
router.register(r'generos', views.GeneroView, 'genero')
router.register(r'razas', views.RazaView, 'raza')
router.register(r'mascotas', views.MascotaView, 'mascota')
router.register(r'desparasitantes', views.DesparasitanteView, 'desparasitante')
router.register(r'desparasitaciones', views.FichaDesparacitacionView, 'fichadesparacitacion')
router.register(r'estados', views.EstadoView, 'estado')
router.register(r'citas', views.CitaView, 'cita')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Veterinaria API'))
]
