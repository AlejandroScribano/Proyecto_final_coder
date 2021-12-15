
from django import forms
from django.db.models.enums import IntegerChoices
from django.shortcuts import render
from AppCentroSalud.models import CuerpoMedico, Pacientes, Consulta
from AppCentroSalud.forms import CuerpoMedicoFormulario, PacientesFormulario, ConsultaFormulario

# Create your views here.
def inicio(request):
    return render(request, "AppCentroSalud/index.html")
    #return HttpResponse('Vista de inicio')

#def doctores(request):
#    return render(request, "AppCentroSalud/doctores.html")

def doctores(request):

    if request.method == "POST":

        miFormulario = CuerpoMedicoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            datos = CuerpoMedico(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                especialidad = informacion["especialidad"],
                dia_hora_atencion = informacion["dia_hora_atencion"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            datos.save()
            return render(request, "AppCentroSalud/index.html")
            
            
    else:
        miFormulario = CuerpoMedicoFormulario()
        return render(request, 'AppCentroSalud/doctores.html',{"miFormulario":miFormulario})

    
def pacientes(request):

    if request.method == "POST":

        miFormulario = PacientesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
           

            datos = Pacientes(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                documento = informacion["documento"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            datos.save()
            return render(request, 'AppCentroSalud/index.html')
            
            
    else:
        miFormulario = PacientesFormulario()
        return render(request, 'AppCentroSalud/pacientes.html',{"miFormulario":miFormulario})


def consultas(request):

    if request.method == "POST":

        miFormulario = ConsultaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            

            datos = Consulta(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                email = informacion["email"],
                telefono = informacion["telefono"],
                consulta_paciente = informacion["consulta_paciente"]
            )
            datos.save()
            return render(request, 'AppCentroSalud/index.html')
            
            
    else:
        miFormulario = ConsultaFormulario()
        return render(request, 'AppCentroSalud/consultas.html',{"miFormulario":miFormulario})


