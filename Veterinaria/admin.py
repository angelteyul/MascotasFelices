from django.contrib import admin
from .models import Dueno, Especie, Genero, Raza, Mascota, Desparasitante, FichaDesparasitacion, Estado, Cita

# Register your models here.
admin.site.register(Dueno)
admin.site.register(Especie)
admin.site.register(Genero)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(Desparasitante)
admin.site.register(FichaDesparasitacion)
admin.site.register(Estado)
admin.site.register(Cita)
