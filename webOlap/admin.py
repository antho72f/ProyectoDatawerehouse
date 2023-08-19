from django.contrib import admin
from .models import *

admin.site.register(RealState)
admin.site.register(DimTiempo)
admin.site.register(DimUbicacion)
admin.site.register(DimTamaño)
admin.site.register(DimFacilidades)
admin.site.register(DimVenta)
admin.site.register(HechosVentas)