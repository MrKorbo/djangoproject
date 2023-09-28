from django.contrib import admin
from .models import user, categoria, producto, detalle_orden, orden
# Register your models here.

admin.site.register(user)
admin.site.register(categoria)
admin.site.register(producto)

admin.site.register(detalle_orden)
admin.site.register(orden)
