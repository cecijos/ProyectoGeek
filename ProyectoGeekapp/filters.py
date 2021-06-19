import django_filters

from .models import *

class ComentarioFilter(django_filters.FilterSet):
 class Meta:
     model=Comentario
     fields= ['Nombre_sala']