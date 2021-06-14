

# Register your models here.
from django.contrib import admin

from .models import Videojuego
from .models import Sala
from .models import Comentario



class VideojuegoAdmin(admin.ModelAdmin):
    search_fields = ['videojuego_id', 'name']


class SalaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'Nombre_juego']


class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ["Nombre_sala__title"]

    list_display = ['mensaje', 'Nombre_sala', 'added_by']

    ordering = ('mensaje', 'Nombre_sala', 'added_by')


admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Comentario, ComentarioAdmin)