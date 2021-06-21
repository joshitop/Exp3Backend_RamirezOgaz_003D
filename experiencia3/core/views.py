from django.shortcuts import render,redirect
from .models import Input, Personas
from .forms import PersonalForm
from .formss import ReseñaForm

# Create your views here.



def galery(request):
    nombre='José Luis Ramírez'
    personas=Personas.objects.all()
    return render(request, 'galery.html', context={'nom_usuario': nombre, 'datos':personas},
    )
def index(request):
    nombre='Danilo Ogaz'
    return render(request, 'index.html', context={'nom_usuario': nombre}, 
    )
def who(request):
    nombre='José Luis'
    return render(request, 'who.html', context={'nom_usuario': nombre}, 
    )
def foro(request):
    nombre='José Ramírez'
    foro=Input.objects.all()
    return render(request, 'foro.html', context={'nom_usuario': nombre, 'date': foro}, 
    )
def crearPersonal(request):
    if request.method=='POST':
        personal_form = PersonalForm(request.POST)
        if personal_form.is_valid():
            personal_form.save()
            return redirect('index')
    else:
        personal_form=PersonalForm()
    return render(request,'core/form_persona.html', {'personal_form': personal_form})



def crearReseña(request):
    if request.method=='POST':
        reseña_form = ReseñaForm(request.POST)
        if reseña_form.is_valid():
            reseña_form.save()
            return redirect('foro')
    else:
        reseña_form=ReseñaForm()
    return render(request,'core/form_reseña.html', {'reseña_form': reseña_form})

def modificarReseña(request, id):
    reseña = Input.objects.get(nombreUsuario=id)
    datos = {
        'form': ReseñaForm(instance=reseña)
    }
    if request.method =='POST':
        formulario = ReseñaForm(data=request.POST, instance = reseña)
        if formulario.is_valid:
            formulario.save()
            return redirect ('foro')
            datos['mensaje'] = "Datos modificados correctamente"
    return render(request,'core/form_mod_reseña.html', datos)

def eliminarReseña(request,id):
    reseña = Input.objects.get(nombreUsuario=id)
    reseña.delete()
    return redirect(to="foro")
