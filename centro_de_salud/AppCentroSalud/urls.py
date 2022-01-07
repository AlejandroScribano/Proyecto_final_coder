from django.urls import path
from AppCentroSalud import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    
    #Path doctores
    path('doctores',views.doctores, name="Doctores"),

    #path pacientes
    path('pacientes',views.pacientes, name="Pacientes"),

    #path consultas
    path('consultas',views.consultas, name="Consultas"),

    #path Acerca de Nosotros
    path('acerca',views.acerca, name="Acerca"),

    #path para Login
    path('login', views.login_request, name='Login'),

    #path para registro
    path('register', views.register, name='Register'),

]