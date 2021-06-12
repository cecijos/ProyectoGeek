from rest_framework import serializers
from .models import Videojuego
from .models import Sala
from .models import Comentario



class VideojuegoSerializer (serializers.ModelSerializer):

    class Meta:
        model=Videojuego
        fields = '__all__'


class SalaSerializer (serializers.ModelSerializer):

    class Meta:
        model=Sala
        fields = '__all__'

class ComentarioSerializer (serializers.ModelSerializer):

    class Meta:
        model=Comentario
        fields = '__all__'