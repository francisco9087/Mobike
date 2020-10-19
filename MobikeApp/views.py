from django.shortcuts import render
from django.http import  HttpRequest
from MobikeApp.forms import FormularioIngresoCliente
# Create your views here.

class FormularioIngresoClienteView(HttpRequest):  
  
    def ingreso_cliente(request):
        cliente = FormularioIngresoCliente()
        return render(request,"MobikeApp/ingreso_cliente.html", {"form":cliente})




    def procesar_formulario(request):
        cliente = FormularioIngresoCliente(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = FormularioIngresoCliente()
        return render(request,"MobikeApp/ingreso_cliente.html", {"form":cliente, "mensaje": 'OK'})  
        