from django.contrib import admin
from .models import Especialidad, Personas, Reseña, Input

# Register your models here.

admin.site.register(Especialidad)
admin.site.register(Personas)
admin.site.register(Reseña)
admin.site.register(Input)