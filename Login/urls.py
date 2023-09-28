from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    path('logout', views.Logout.as_view(), name='logout'),
    path('producto/', views.Producto.as_view(), name='producto'),
    path('crear/', views.Crear.as_view(), name='crear'),
    path('editar/<int:id>', views.Editar, name='editar'),
    path('eliminar/<int:id>', views.Eliminar, name='eliminar'),
    path('ticket/', views.mostrar_detalle_orden, name='ticket'),
    path('crear/detalle_orden', views.crear_detalle_orden.as_view(), name='crear_detalle_orden'),
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),
]