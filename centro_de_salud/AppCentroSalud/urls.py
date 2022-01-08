from django.urls import path
from AppCentroSalud import views
#para el logout
from django.contrib.auth.views import LogoutView

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

    #path para el logout
    path('logout', LogoutView.as_view(template_name = 'AppCentroSalud/logout.html'), name='Logout'),

    #path para editar usuario
    path('editarUsuario', views.editarUsuario, name='EditarUsuario'),

]