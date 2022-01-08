# 
from django import forms
from django.db.models.enums import IntegerChoices
from django.shortcuts import render
from AppCentroSalud.models import Persona, Medico, Consulta

# Create your views here.
def inicio(request):
    return render(request, "AppCentroSalud/index.html")
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

def doctores_modificar(request):
    return render(request, 'AppCentroSalud/doctores_modificar.html')

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
def pacientes_insertar(request):

    if request.method == "POST":
        personaInst =Persona (nombre = request.POST['inputNombre'],
            apellido = request.POST['inputApellido'],
            documento = request.POST['inputDocumento'],
            email = request.POST['inputEmail'],
            telefono = request.POST['inputTelefono'])
        personaInst.save()
        return render(request, "AppCentroSalud/pacientes_insertar.html")

    return render(request, 'AppCentroSalud/pacientes_insertar.html')

def pacientes_eliminar(request, id_para_eliminar):
    pacienteEliminar = Persona.objects.get(documento=id_para_eliminar)
    pacienteEliminar.delete()
    pacientesInst = Persona.objects.all()

    dir = {"pacientesInst": pacientesInst}

    return render(request, 'AppCentroSalud/pacientes_leer.html',dir)

def pacientes_modificar(request):
        return render(request, 'AppCentroSalud/pacientes_modificar.html')

def pacientes_leer(request):

    pacientesInst = Persona.objects.all()

    dir = {"pacientesInst": pacientesInst}

    return render(request, 'AppCentroSalud/pacientes_leer.html',dir)

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
    return render(request, "AppCentroSalud/acerca.html")
