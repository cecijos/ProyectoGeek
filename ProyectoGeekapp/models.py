

# Create your models here.


# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone



class Videojuego(models.Model):
    videojuego_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name




class Sala(models.Model):
    title = models.CharField(max_length=200)

    Nombre_juego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Comentario(models.Model):
    mensaje = models.CharField(max_length=200)
    Nombre_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.mensaje
