


# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate,logout
from .models import Videojuego
from .models import Sala
from .models import Comentario
from django.contrib.auth.forms import UserCreationForm

from .forms import SalaForm
from .forms import ComentarioForm
from django.contrib import messages
from .filters import ComentarioFilter
from django.views.generic import ListView






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

def log_out(request):
    logout(request)
    return redirect('login')






class HomeView (ListView):
    model=Comentario
    template_name='mytemplates/home.html'
    ordering=['-id']
    search_fields = ["Nombre_sala__title"]


def filterchats (request):
    chats=Comentario.objects.all()
    filtercoment=ComentarioFilter(request.GET,queryset=chats)

    return render(request,'mytemplates/busqueda.html',{'filter':filtercoment})





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




