from django.db import models

class Dueno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'apellido', 'correo_electronico'], name='unique_cita')
        ]
        
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.correo_electronico}'


class Especie(models.Model):
    id = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.especie


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.genero


class Raza(models.Model):
    id = models.AutoField(primary_key=True)
    raza = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.raza

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre


class Desparasitante(models.Model):
    id = models.AutoField(primary_key=True)
    desparasitante = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.desparasitante


class FichaDesparasitacion(models.Model):
    id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    desparasitante = models.ForeignKey(Desparasitante, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=100)
    notas = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['mascota', 'fecha', 'desparasitante'], name='unique_ficha_desparasitante')
        ]
        
    def __str__(self) -> str:
        return f'{self.mascota} - {self.fecha}'


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100, default='Pendiente', choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')])
    
    def __str__(self) -> str:
        return self.estado


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_y_hora = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    notas = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.dueno} - {self.mascota} - {self.fecha_y_hora}'
