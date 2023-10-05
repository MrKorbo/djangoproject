from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    path('logout', views.Logout.as_view(), name='logout'),
    path('producto/', views.Producto.as_view(), name='producto'),
    path('crear/', views.Crear.as_view(), name='crear'),
    path('crear/detalle_orden', views.crear_detalle_orden.as_view(), name='crear_detalle_orden'),
    path('editar/<int:id>', views.Editar, name='editar'),
    path('eliminar/<int:id>', views.Eliminar, name='eliminar'),
<<<<<<< Updated upstream
    path('ticket/', views.mostrar_detalle_orden, name='ticket'),
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),
=======

    path('crear/detalle_orden/', views.crear_detalle_orden.as_view(), name='crear_detalle_orden'),
    path('mostrar_ordenes/', views.mostrar_ordenes, name='mostrar_ordenes'),
    path('insertarDato/', views.insertar_dato, name='insertarDato'),
    path('guardarItem/', views.guardar_items, name='guardarItem'),
    path('vistaOrden/', views.vistaOrden.as_view(), name='vistaOrden'),

>>>>>>> Stashed changes
]