from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Especialidad, Personas 


class PersonalForm(forms.ModelForm):
    class Meta:
        model=Personas
        fields=['nombre','edad','especialidad','descrip','image',]
        labels={
            'nombre': 'Nombre',
            'edad': 'Edad',
            'especialidad': 'Especialidad',
            'descrip': 'Descripcion',
            'image': 'Imagen',

        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id': 'nombre'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Edad',
                    'id': 'edad'
                }
            ),
            'especialidad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'especialidad'
                }
            ),
            'descrip': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción',
                    'id': 'edad'
                }
            ),
            'image': forms.ImageField(
            widget=forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'image'
                }
            ))           
        }
        