from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

import datetime

from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    ultimas_publicaciones = Publicaciones.objects.order_by('-id')[0:3] 
    total_publicaciones = Publicaciones.objects.count()
    comentarios = Comentario.objects.order_by('-id')[0:3]    

    usuarios = User.objects.all()        
    total_usuarios = usuarios.count()    

    if request.method == "POST":
        
        comentario = CrearComentario(request.POST)
        
        if comentario.is_valid():

            informacion = comentario.cleaned_data

            comentario_nuevo = Comentario(comentario=informacion['comentario'], autor=request.user, fecha=datetime.datetime.today())
            comentario_nuevo.save()

            messages.success(request, "El comentario fue publicado.") 
            return redirect('inicio')
        
        return render(request, "MillasViajerasApp/index.html", {"comentario":comentario})
    
    comentario = CrearComentario() 
    return render(request, "MillasViajerasApp/index.html", {'total_usuarios':total_usuarios, 'total_publicaciones':total_publicaciones, 'comentario':comentario, 'comentarios':comentarios, "ultimas_publicaciones":ultimas_publicaciones})

def publicaciones(request):
        publicaciones = Publicaciones.objects.all().order_by('-id')

        return render(request, "MillasViajerasApp/publicaciones.html", {"publicaciones":publicaciones})

def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')            
            else:
                return redirect('login')
        
        return render(request, 'MillasViajerasApp/registro.html', {"form":form})
    
    form = UserRegisterForm()
    return render(request, 'MillasViajerasApp/registro.html', {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)                
                return redirect("inicio")
            else:                
                return redirect("login")
                
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"MillasViajerasApp/login.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']                                

            user.save()

            messages.success(request, "Los cambios fueron actualizados.") 
            return redirect('editar_perfil')

    else:
        form = UserEditForm(initial={'email':user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render (request, 'MillasViajerasApp/editarPerfil.html', {"form":form})

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            avatar = Avatar(user=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            messages.success(request, "El avatar se agrego exitosamente.") 
            return redirect("editar_perfil")

    else:

        form = AvatarForm()

    
    return render(request, "MillasViajerasApp/agregar_avatar.html", {"form":form})

class cambiar_password(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('editar_perfil') 

    def get_context_data(self, *args, **kwargs):
        contexto = super(cambiar_password, self).get_context_data()
        mensaje = messages.success(self.request, 'La contraseña se cambio correctamente')

        contexto['mensaje']=mensaje

        return contexto

@login_required
def crear_publicacion(request):   
   
    if request.method == "POST":
        
        publicacion = CrearPublicacion(request.POST, request.FILES)
        
        if publicacion.is_valid():

            informacion = publicacion.cleaned_data

            publicacion_nueva = Publicaciones(imagen=informacion["imagen"],pais=informacion["pais"], titulo=informacion["titulo"], descripcion=informacion["descripcion"], fecha_viaje=datetime.datetime.today(), autor=request.user)
            publicacion_nueva.save()

            messages.success(request, "La publicacion se creo exitosamente.") 
            return redirect('mis_publicaciones')
        
        return render(request, "MillasViajerasApp/crearpublicacion.html", {"publicacion":publicacion})
    
    publicacion = CrearPublicacion()
    return render(request, 'MillasViajerasApp/crearpublicacion.html', {'publicacion':publicacion})

@login_required
def mis_publicaciones(request):
    publicaciones = Publicaciones.objects.filter(autor=request.user).order_by('-id')        

    return render(request, "MillasViajerasApp/mis_publicaciones.html", {"publicaciones":publicaciones})

def about(request):

    return render(request, "MillasViajerasApp/about.html", {})

class ver_publicacion(DetailView):

    model = Publicaciones
    template_name = "MillasViajerasApp/ver_publicacion.html"  

    def get_context_data(self, *args, **kwargs):
        contexto = super(ver_publicacion, self).get_context_data()

        publicacion = get_object_or_404(Publicaciones, id=self.kwargs['pk'])
        total_likes = publicacion.total_likes()
        contexto['total_likes'] = total_likes

        return contexto

@login_required
def editar_publicacion(request, publicacion_id):
    
    publicacion = Publicaciones.objects.get(id=publicacion_id)

    if request.method == "POST":

        formulario = CrearPublicacion(request.POST, request.FILES)

        if formulario.is_valid():

            info_publicacion = formulario.cleaned_data

            publicacion.imagen = info_publicacion["imagen"]
            publicacion.pais = info_publicacion["pais"]
            publicacion.titulo = info_publicacion["titulo"]
            publicacion.descripcion = info_publicacion["descripcion"]           

            publicacion.save()
            messages.success(request, "La publicacion se edito exitosamente.") 
            
            return redirect ("mis_publicaciones")

    
    formulario = CrearPublicacion(initial={"pais":publicacion.pais, "titulo":publicacion.titulo, "descripcion":publicacion.descripcion, "fecha_viaje":datetime.datetime.today()})

    return render (request, "MillasViajerasApp/editar_publicacion.html", {"form":formulario})

@login_required
def eliminar_publicacion(request, publicacion_id):

    publicacion = Publicaciones.objects.get(id=publicacion_id)
    publicacion.delete()

    messages.success(request, "La publicacion se elimino exitosamente.") 
    return redirect("mis_publicaciones")

@login_required
def crear_comentario(request):

    if request.method == "POST":
        
        comentario = CrearComentario(request.POST)
        
        if comentario.is_valid():

            informacion = comentario.cleaned_data

            comentario_nuevo = Comentario(comentario=informacion['comentario'], autor=request.user)
            comentario_nuevo.save()

            messages.success(request, "El comentario fue publicado.") 
            return redirect('inicio')
        
        return render(request, "MillasViajerasApp/index.html", {"comentario":comentario})
    
    comentario = CrearComentario()
    return render(request, 'MillasViajerasApp/index.html', {'comentario':comentario})

@login_required
def publicaciones_like(request, pk):

    publicacion = get_object_or_404(Publicaciones, pk=pk)
    publicacion.likes.add(request.user)

    return HttpResponseRedirect(reverse('ver_publicacion', args=[str(pk)]))

@login_required
def agregar_comentario_publicacion(request, pk):

    if request.method == "POST":
        
            comentario = AgregarComentario(request.POST)
        
            if comentario.is_valid():

                informacion = comentario.cleaned_data

                comentario_nuevo = ComentarioPublicacion(publicacion=get_object_or_404(Publicaciones, pk=pk), nombre=request.user, comentario=informacion['comentario'], fecha=datetime.datetime.today())
                comentario_nuevo.save()
                
                return redirect('publicaciones')
        
            return render(request, "MillasViajerasApp/publicacionComentario.html", {"comentario":comentario})
    
    comentario = AgregarComentario()
    return render(request, 'MillasViajerasApp/publicacionComentario.html', {"comentario":comentario})
