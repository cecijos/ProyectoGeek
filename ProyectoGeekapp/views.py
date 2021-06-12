from django.shortcuts import render

# Create your views here.



from .serializers import  VideojuegoSerializer
from .serializers import SalaSerializer
from .serializers import ComentarioSerializer
from .models import Videojuego
from .models import Sala
from .models import Comentario


from rest_framework import viewsets




class VideojuegoViewSet (viewsets.ModelViewSet):
    queryset = Videojuego.objects.all
    serializer_class = VideojuegoSerializer



class SalarViewSet (viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
        queryset = Comentario.objects.all()

        serializer_class = ComentarioSerializer







