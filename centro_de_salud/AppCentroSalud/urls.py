from django.urls import path
from AppCentroSalud import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    
    #Path doctores
    path('doctores_insertar',views.doctores_insertar, name="doctoresInsertar"),

    path('doctores_eliminar/<id_para_eliminar>',views.doctores_eliminar, name="doctoresEliminar"),

    path('doctores_modificar',views.doctores_modificar, name="doctoresModificar"),

    path('doctores_leer',views.doctores_leer, name="doctoresLeer"), 

    #path pacientes
    path('pacientes_insertar',views.pacientes_insertar, name="pacientesInsertar"),

    path('pacientes_eliminar/<id_para_eliminar>',views.pacientes_eliminar, name="pacientesEliminar"),

    path('pacientes_modificar',views.pacientes_modificar, name="pacientesModificar"),

    path('pacientes_leer',views.pacientes_leer, name="pacientesLeer"),

    #path consultas
    path('consultas_insertar',views.consultas_insertar, name="consultasInsertar"),

    path('consultas_eliminar/<id_para_eliminar>',views.consultas_eliminar, name="consultasEliminar"),

    path('consultas_modificar',views.consultas_modificar, name="consultasModificar"),

    path('consultas_leer',views.consultas_leer, name="consultasLeer"),

    #path Acerca de Nosotros
    path('acerca',views.acerca, name="Acerca"),

]