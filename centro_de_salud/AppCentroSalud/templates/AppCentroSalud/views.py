from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppCentroSalud/index.html")
    #return HttpResponse('Vista de inicio')

def doctores(request):
    return render(request, "AppCentroSalud/doctores.html")
    
def pacientes(request):
    return render(request, "AppCentroSalud/pacientes.html")

def consultas(request):
    return render(request, "AppCentroSalud/consultas.html")
