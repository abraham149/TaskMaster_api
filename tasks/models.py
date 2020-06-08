# todos/models.py
from django.db import models
from django.conf import settings


class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
    terminada = models.BooleanField(default=False)
    fechaTerminada = models.CharField(max_length=200)

    def __str__(self):
        """A string representation of the model."""
        return self.titulo