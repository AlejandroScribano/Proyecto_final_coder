
from django import forms
from django.db.models.enums import IntegerChoices
from django.shortcuts import render
#para el Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash

#para decorador
from django.contrib.auth.decorators import login_required


from AppCentroSalud.models import Medico, Persona, Consulta, Avatar
from AppCentroSalud.forms import CuerpoMedicoFormulario, PacientesFormulario, ConsultaFormulario, UserRegisterForm, UserEditForm

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

def doctores(request):

    # if request.method == "POST":

    #     miFormulario = CuerpoMedicoFormulario(request.POST)

    #     if miFormulario.is_valid():
    #         informacion = miFormulario.cleaned_data
            
    #         datos = CuerpoMedico(
    #             nombre = informacion["nombre"],
    #             apellido = informacion["apellido"],
    #             especialidad = informacion["especialidad"],
    #             dia_hora_atencion = informacion["dia_hora_atencion"],
    #             email = informacion["email"],
    #             telefono = informacion["telefono"]
    #         )
    #         datos.save()
    #         return render(request, "AppCentroSalud/doctores.html")
            
            
    # else:
    #     miFormulario = CuerpoMedicoFormulario()
    #     return render(request, 'AppCentroSalud/doctores.html',{"miFormulario":miFormulario})
    return render(request, 'AppCentroSalud/doctores.html')

    
def pacientes(request):

    # if request.method == "POST":

    #     miFormulario = PacientesFormulario(request.POST)

    #     if miFormulario.is_valid():
    #         informacion = miFormulario.cleaned_data
           

    #         datos = Pacientes(
    #             nombre = informacion["nombre"],
    #             apellido = informacion["apellido"],
    #             documento = informacion["documento"],
    #             email = informacion["email"],
    #             telefono = informacion["telefono"]
    #         )
    #         datos.save()
    #         return render(request, 'AppCentroSalud/pacientes.html')
            
            
    # else:
    #     miFormulario = PacientesFormulario()

        #return render(request, 'AppCentroSalud/pacientes.html',{"miFormulario":miFormulario})
        return render(request, 'AppCentroSalud/pacientes.html')


def consultas(request):

    # if request.method == "POST":

    #     miFormulario = ConsultaFormulario(request.POST)

    #     if miFormulario.is_valid():
    #         informacion = miFormulario.cleaned_data
            

    #         datos = Consulta(
    #             nombre = informacion["nombre"],
    #             apellido = informacion["apellido"],
    #             email = informacion["email"],
    #             telefono = informacion["telefono"],
    #             consulta_paciente = informacion["consulta_paciente"]
    #         )
    #         datos.save()
    #         return render(request, 'AppCentroSalud/consultas.html')
            
            
    # else:
    #     miFormulario = ConsultaFormulario()
    #     return render(request, 'AppCentroSalud/consultas.html',{"miFormulario":miFormulario})
    return render(request, 'AppCentroSalud/consultas.html')

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
                return render(request, 'AppCentroSalud/index.html', {"mensaje": f"Bienvenido {usuario}"})
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

            return render(request, 'AppCentroSalud/index.html')
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
