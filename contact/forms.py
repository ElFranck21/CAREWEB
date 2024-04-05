from django import forms
from .models import Contacto


class Contacto (forms.Form):
    nombre=forms.CharField(max_length=100)
    correo=forms.EmailField()
    descripcion=forms.CharField(max_length=1000)

class ContactoForm(forms.ModelForm):

    class Meta:
        model= Contacto
        fields=["nombre", "correo", "descripcion"]