from django.shortcuts import render, redirect

# Create your views here.



from django.contrib.auth import login, authenticate
from .models import Videojuego
from .models import Sala
from .models import Comentario
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import SalaForm
from .forms import ComentarioForm
from django.contrib import messages
from .filters import ComentarioFilter
from django.views.generic import ListView



from rest_framework import viewsets

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()
    return render (request,'mytemplates/register.html', {'form': f})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'mytemplates/login.html', context)

class VideojuegoViewSet (viewsets.ModelViewSet):
    queryset = Videojuego.objects.all




class SalarViewSet (viewsets.ModelViewSet):
    queryset = Sala.objects.all()


class ComentarioViewSet(viewsets.ModelViewSet):
        queryset = Comentario.objects.all()





#def home(request):
    #return  HttpResponse ('Home Page')
class HomeView (ListView):
    model=Comentario
    template_name='mytemplates/home.html'
    ordering=['-id']


def createSala(request):
    form=SalaForm()
    if request.method=='POST':
        #print('PRINT POST',request.POST)
        form=SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'mytemplates/sala_form.html',context)


def createComentario(request):
    form=ComentarioForm()
    if request.method=='POST':
        #print('PRINT POST',request.POST)
        form=ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'mytemplates/comentario_form.html',context)


def UpdateComentario(request,pk):
    comentario=Comentario.objects.get(id=pk)
    form=ComentarioForm(instance=comentario)
    if request.method=='POST':
        #print('PRINT POST',request.POST)
        form=ComentarioForm(request.POST,instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'mytemplates/comentario_form.html',context)
def BorrarComentario(request,pk):
    comentario = Comentario.objects.get(id=pk)
    if request.method=="POST":
        comentario.delete()
        return redirect('/')

    context={'item':comentario}
    return render(request,'mytemplates/BorrarComentario.html',context)

#def contact(request):
    #return  render (request,'mytemplates/register.html')



