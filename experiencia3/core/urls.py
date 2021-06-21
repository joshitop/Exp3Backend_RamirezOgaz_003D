from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('galery/',views.galery, name='galery'),
    path('who/',views.who, name='who'),
    path('foro/',views.foro, name='foro'),
    path('agregar_personal/',views.crearPersonal, name="crearPersonal"),
    path('agregar_reseña/',views.crearReseña, name="crearReseña"),
    path('modificar_reseña/<id>',views.modificarReseña, name="modificarReseña"),
    path('eliminar_reseña/<id>',views.eliminarReseña, name="eliminarReseña"),

]


