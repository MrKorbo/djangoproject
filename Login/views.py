from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import user, producto, detalle_orden, orden
from .forms import ProductoForm, DetalleOrdenForm

#===========================================================================================================================
# Vistas
#=========================================================================================================================== 

class Login(LoginView):
    next_page = reverse_lazy('inicio')
    template_name = 'vistas/login.html'

#--------------------------------------------------------------------------------------------------------------------------

class Logout(LogoutView):
    next_page = reverse_lazy('login')

#--------------------------------------------------------------------------------------------------------------------------

class Inicio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'vistas/inicio.html'

#--------------------------------------------------------------------------------------------------------------------------

class Producto(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'vistas/producto.html'

    def get(self, request, *args, **kwargs):
        productos = producto.objects.all() 
        return render(request, self.template_name, {'Producto': productos})
    
#===========================================================================================================================
# Orden
#=========================================================================================================================== 

class crear_detalle_orden(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'orden/crear_detalle_orden.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = producto.objects.all()  # Agrega los productos al contexto
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = DetalleOrdenForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mostrar_ordenes')
        else:
            form = DetalleOrdenForm()

        return render(request, 'orden/crear_detalle_orden.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------------------
    
def mostrar_ordenes(request):
    ordenes = orden.objects.all()
    return render(request, 'orden/orden.html', {'mostrarOrdenes': ordenes})

#--------------------------------------------------------------------------------------------------------------------------

class vistaOrden(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'orden/vista_orden.html'

    def get(self, request, *args, **kwargs):
        detalle = detalle_orden.objects.all() 
        return render(request, 'orden/vista_orden.html' , {'detalles': detalle})
    
#===========================================================================================================================
# Productos
#=========================================================================================================================== 

class Crear(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'productos/crear.html'
    def post(self, request, *args, **kwargs):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            producto = formulario.save()
            return redirect('producto')
        else:
            return render(request, 'productos/crear.html', {'formulario': formulario})
        
#--------------------------------------------------------------------------------------------------------------------------
        
def Editar(request, id):
    producto_editar = producto.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto_editar)
        if formulario.is_valid():
            formulario.save()
            return redirect('producto')
    else:
        formulario = ProductoForm(instance=producto_editar)

    return render(request, 'productos/editar.html', {'formulario': formulario})

#--------------------------------------------------------------------------------------------------------------------------

def Eliminar(request, id):
    Producto=producto.objects.get(id=id)
    Producto.delete()
    return redirect('producto')

#===========================================================================================================================
# JAVASCRIPT
#===========================================================================================================================

@csrf_exempt  # Deshabilita la protección CSRF para esta vista (deberías habilitarla adecuadamente en producción)
def insertar_dato(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del cuerpo de la solicitud POST
            data = json.loads(request.body)
            
            # Realiza la inserción de datos en el modelo (ajusta esto según tus modelos)
            nuevo_dato = orden(fecha=data['fecha'], receptor=data['receptor'], tipo=data['tipo'])
            nuevo_dato.save()
            
            return JsonResponse({'mensaje': 'Dato insertado correctamente', 'id': nuevo_dato.id})        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)  # Responde con un mensaje de error en caso de problemas
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)  # Responde con un error si la solicitud no es POST
    
#--------------------------------------------------------------------------------------------------------------------------

@csrf_exempt  # Deshabilita la protección CSRF para esta vista (deberías habilitarla adecuadamente en producción)
def guardar_items(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        for item_data in data['productos']:
                producto_id = item_data['producto']
                cantidad = item_data['cantidad']

                # Crear un nuevo objeto DetalleOrden y guardarlo en la base de datos
                detalle = detalle_orden(producto=producto_id, cantidad = cantidad, orden=data.get('id_orden'))
                detalle.save()
        
        return JsonResponse({'mensaje': 'Datos guardados correctamente'})
    
    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    
#===========================================================================================================================