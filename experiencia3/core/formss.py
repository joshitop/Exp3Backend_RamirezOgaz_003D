from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Reseña, Input



class ReseñaForm(forms.ModelForm):
    nombreUsuario = forms.CharField(label='Nombre', min_length=3, max_length=40, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Nombre'
        }
    ))
    edad = forms.IntegerField(label='Edad',  widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Edad'
        }
    ))
    correoElectronico = forms.EmailField(label='Correo Electrónico',  widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        }
    ))
    personalContratado = forms.CharField(label='Personal Contratado',  widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del personal'
        }
    ))
    numeroEstrellas = forms.ModelChoiceField(queryset=Reseña.objects.all(),label='Número de Estrellas',  widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))
    comentario = forms.CharField(label='Deja aquí tu comentario', max_length=200,  widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Comentario'
        }
    ))
    class Meta:
        model=Input
        fields=['nombreUsuario','edad','correoElectronico','personalContratado','numeroEstrellas','comentario']
        