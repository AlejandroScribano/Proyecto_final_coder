# 
from django import forms
from django.db.models.enums import IntegerChoices
from django.shortcuts import render
#para el Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash

#para decorador
from django.contrib.auth.decorators import login_required

#para el agregar avatar
from django.contrib.auth.models import User

from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView


from AppCentroSalud.models import Medico, Persona, Consulta, Avatar
from AppCentroSalud.forms import MedicoFormulario, PacientesFormulario, ConsultaFormulario, UserRegisterForm, UserEditForm, AvatarFormulario

# Create your views here.


def inicio(request):
    #Para mostar avatar
    diccionario = {}
    cantidadAvatares = 0
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user = request.user.id)
        for a in avatar:
            cantidadAvatares = cantidadAvatares + 1
        if cantidadAvatares > 0:
            diccionario["avatar"] = avatar[cantidadAvatares-1].imagen.url

        #diccionario["avatar"] = avatar[cantidadAvatares-1].imagen.url

    return render(request, "AppCentroSalud/index.html", diccionario)
    #return HttpResponse('Vista de inicio')

#def doctores(request):
#    return render(request, "AppCentroSalud/doctores.html")

def doctores_insertar(request):

    if request.method == "POST":
        doctoresInst =Medico (nombre = request.POST['inputNombre'],
            apellido = request.POST['inputApellido'],
            documento = request.POST['inputDocumento'],
            email = request.POST['inputEmail'],
            telefono = request.POST['inputTelefono'],
            especialidad = request.POST['selectEspecialidad'])
        doctoresInst.save()
        return render(request, "AppCentroSalud/doctores_insertar.html")

    return render(request, 'AppCentroSalud/doctores_insertar.html')

def doctores_eliminar(request, id_para_eliminar):

    doctorEliminar = Medico.objects.get(documento=id_para_eliminar)
    doctorEliminar.delete()
    doctoresInst = Medico.objects.all()

    dir = {"doctoresInst": doctoresInst}

    return render(request, 'AppCentroSalud/doctores_leer.html',dir)

def doctores_modificar(request, id_para_editar):
    doctorModificar = Medico.objects.get(documento=id_para_editar)

    if request.method == "POST":

        print(request.POST)

        miFormulario =MedicoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            doctorModificar.nombre = informacion["nombre"]
            doctorModificar.apellido = informacion["apellido"]
            doctorModificar.documento = informacion["documento"]
            doctorModificar.email = informacion["email"]
            doctorModificar.telefono = informacion["telefono"]
            doctorModificar.especialidad = informacion["especialidad"]



            
            doctorModificar.save()
        return render(request, "AppCentroSalud/index.html")
    else:
        miFormulario = MedicoFormulario (initial={"nombre":doctorModificar.nombre,"apellido":doctorModificar.apellido,"documento":doctorModificar.documento,"email":doctorModificar.email,"telefono":doctorModificar.telefono,"especialidad":doctorModificar.especialidad})

    return render(request, 'AppCentroSalud/doctores_modificar.html',{"miFormulario":miFormulario,"id_para_editar":id_para_editar})
        

def doctores_leer(request):

    doctoresInst = Medico.objects.all()

    dir = {"doctoresInst": doctoresInst}

    return render(request, 'AppCentroSalud/doctores_leer.html',dir)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
# 
# 
# 
# 
# 
#

class PersonaLista(ListView):
    model = Persona
    template_name = "AppCentroSalud/pacientes_leer.html"

#Detalle - SUPER Leer - Buscar!!!!!
class PersonaDetalle(DetailView):
    
    model = Persona
    template_name = "AppCentroSalud/pacientes_detalle.html"
    
#Crear elementos
class PersonaInsertar(CreateView):
    
    model = Persona
    success_url = "pacientes_leer"  #AppCoder/template/AppCoder/editar
    fields = ["nombre", "apellido", "documento", "email", "telefono" ]
    
#modificar!!!!!!!!!!!  
class PersonaModificar(UpdateView):
    
    model = Persona
    success_url = "../pacientes_leer"
    fields = ["nombre", "apellido", "documento", "email", "telefono" ]
  
#Borrar   
class PersonaEliminar(DeleteView):
    
    model = Persona
    success_url = "../pacientes_leer"


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#    



def consultas_insertar(request):

    if request.method == "POST":
        consultaInst =Consulta (nombre = request.POST['inputNombre'],
            apellido = request.POST['inputApellido'],
            email = request.POST['inputEmail'],
            telefono = request.POST['inputTelefono'],
            consulta_paciente = request.POST['textareaConsulta'] )

        consultaInst.save()
        return render(request, "AppCentroSalud/consultas_insertar.html")
    
    return render(request, 'AppCentroSalud/consultas_insertar.html')

def consultas_eliminar(request, id_para_eliminar):
    consultaEliminar = Consulta.objects.get(nombre=id_para_eliminar)
    consultaEliminar.delete()
    consultasInst = Consulta.objects.all()

    dir = {"consultasInst": consultasInst}

    return render(request, 'AppCentroSalud/consultas_leer.html',dir)

def consultas_modificar(request):
    return render(request, 'AppCentroSalud/consultas_modificar.html')

def consultas_leer(request):
    consultasInst = Consulta.objects.all()

    dir = {"consultasInst": consultasInst}

    return render(request, 'AppCentroSalud/consultas_leer.html',dir)

#acerca
def acerca(request):
    #Para mostar avatar
    diccionario = {}
    cantidadAvatares = 0
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user = request.user.id)
        for a in avatar:
            cantidadAvatares = cantidadAvatares + 1
        if cantidadAvatares > 0:
            diccionario["avatar"] = avatar[cantidadAvatares-1].imagen.url

    return render(request, "AppCentroSalud/acerca.html", diccionario)

#Login
def login_request(request):
    if request.method =="POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                #return render(request, 'AppCentroSalud/index.html', {"mensaje": f"Bienvenido {usuario}"})
                return inicio(request) #Llama a la vista de inicio
            else:
                return render(request, 'AppCentroSalud/index.html', {"mensaje": f"Error, datos incorrectos"})
        
        else:
            return render(request, 'AppCentroSalud/index.html', {"mensaje": f"Formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, 'AppCentroSalud/login.html', {'form':form})

#Registro

def register(request):
    #form = UserCreationForm(request.POST)
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        form.save()
        return render(request, "AppCentroSalud/index.html", {"mensaje": "Usuario creado."})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "AppCentroSalud/register.html", {"form":form})

#Edición de usuario

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            #return render(request, 'AppCentroSalud/index.html')
            return inicio(request) #Llama a la vista de inicio
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

        diccionario = {}
        diccionario["miFormulario"] = miFormulario
        diccionario["usuario"] = usuario
        #Para mostar avatar       
        cantidadAvatares = 0
        if request.user.is_authenticated:
            avatar = Avatar.objects.filter(user = request.user.id)
            for a in avatar:
                cantidadAvatares = cantidadAvatares + 1
            if cantidadAvatares > 0:
                diccionario["avatar"] = avatar[cantidadAvatares-1].imagen.url
                  
            

        return render(request, 'AppCentroSalud/editarUsuario.html',diccionario)
        #return render(request, 'AppCentroSalud/editarUsuario.html', {"miFormulario":miFormulario,"usuario":usuario, "avatar" : avatar[cantidadAvatares-1].imagen.url })


#Agregar avatar

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            usuario = User.objects.get(username=request.user)
            avatar = Avatar(user = usuario, imagen = miFormulario.cleaned_data['imagen'])
            avatar.save()

            #return render (request, 'AppCentroSalud/index.html')
            return inicio(request) #Llama a la vista de inicio
            
    else:
        miFormulario = AvatarFormulario()
        diccionario = {}
        diccionario["miFormulario"] = miFormulario

        #Para mostar avatar       
        cantidadAvatares = 0
        if request.user.is_authenticated:
            avatar = Avatar.objects.filter(user = request.user.id)
            for a in avatar:
                cantidadAvatares = cantidadAvatares + 1
            if cantidadAvatares > 0:
                diccionario["avatar"] = avatar[cantidadAvatares-1].imagen.url

        return render(request, 'AppCentroSalud/agregarAvatar.html', diccionario)
        #return render(request, 'AppCentroSalud/agregarAvatar.html', {"miFormulario": miFormulario})
