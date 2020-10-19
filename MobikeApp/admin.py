from django.contrib import admin
from MobikeApp.models import Banco, Cliente, Comuna, Contrato, Estacionamiento, Gps, ReporteUso, TarjetaCredito, TarjetaMuni, Zona, Bicicleta
# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display =  ("rut", "nombres", "apellidos","email", "contrasena")
    list_filter =("email",)
    search_fields = ("nombres",)

admin.site.register(Banco)

admin.site.register(Cliente,ClientesAdmin)

admin.site.register(Comuna)

admin.site.register(Contrato)

admin.site.register(Estacionamiento)

admin.site.register(Gps)

admin.site.register(ReporteUso)

admin.site.register(TarjetaCredito)

admin.site.register(TarjetaMuni)

admin.site.register(Zona)

admin.site.register(Bicicleta)