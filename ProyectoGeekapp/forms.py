from django.forms import ModelForm
from .models import Sala
from .models import Comentario

class SalaForm(ModelForm):
    class Meta:
        model=Sala
        fields='__all__'

class ComentarioForm(ModelForm):
    class Meta:
        model=Comentario
        fields='__all__'