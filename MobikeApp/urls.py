from django.urls import path

from MobikeApp import views

urlpatterns = [
    
    path('ingreso_cliente/', views.FormularioIngresoClienteView.ingreso_cliente, name = "ingreso_cliente"),
    path('guardar_cliente/', views.FormularioIngresoClienteView.procesar_formulario, name = "guardar_cliente"),
]
