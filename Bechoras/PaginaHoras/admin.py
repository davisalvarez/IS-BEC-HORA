from django.contrib import admin
from .models import Usuario
from .models import Actividad
from .models import AsigActividad

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(AsigActividad)
