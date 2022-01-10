from django.urls import path
from AppCentroSalud import views
#para el logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    
    #Path doctores
    path('doctores_insertar',views.doctores_insertar, name="doctoresInsertar"),

    path('doctores_eliminar/<id_para_eliminar>',views.doctores_eliminar, name="doctoresEliminar"),

    path('doctores_modificar/<id_para_editar>',views.doctores_modificar, name="doctoresModificar"),

    path('doctores_leer',views.doctores_leer, name="doctoresLeer"), 

    #path pacientes
    path('pacientes_insertar',views.pacientes_insertar, name="pacientesInsertar"),

    path('pacientes_eliminar/<id_para_eliminar>',views.pacientes_eliminar, name="pacientesEliminar"),

    path('pacientes_modificar/<id_para_editar>',views.pacientes_modificar, name="pacientesModificar"),

    path('pacientes_leer',views.pacientes_leer, name="pacientesLeer"),

    #path consultas
    path('consultas_insertar',views.consultas_insertar, name="consultasInsertar"),

    path('consultas_eliminar/<id_para_eliminar>',views.consultas_eliminar, name="consultasEliminar"),

    path('consultas_modificar',views.consultas_modificar, name="consultasModificar"),

    path('consultas_leer',views.consultas_leer, name="consultasLeer"),

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