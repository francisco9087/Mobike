from django import forms

from MobikeApp.models import Cliente

class FormularioIngresoCliente (forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[ 
            'rut',
            'dv',
            'nombres',
            'apellidos',
            'email', 
            'contrasena']
        widgets = {'contrasena': forms.PasswordInput(),
                    'email': forms.EmailInput()    }
        
       