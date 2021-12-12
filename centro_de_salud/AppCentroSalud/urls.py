from django.urls import path
from AppCentroSalud import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
]