from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import user, producto, categoria, detalle_orden, orden
from .forms import ProductoForm, DetalleOrdenForm

class Login(LoginView):
    next_page = reverse_lazy('inicio')
    template_name = 'vistas/login.html'    

class Logout(LogoutView):
    next_page = reverse_lazy('login')

class Inicio(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'vistas/inicio.html'

class Producto(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'vistas/producto.html'

    def get(self, request, *args, **kwargs):
        productos = producto.objects.all() 
        return render(request, self.template_name, {'Producto': productos})
#==============================================================================================
def mostrar_detalle_orden(request):
    detalle_ordenes = detalle_orden.objects.all()
    return render(request, 'productos/detalle_orden.html', {'detalle_ordenes': detalle_ordenes})

class crear_detalle_orden(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'productos/crear_detalle_orden.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = DetalleOrdenForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('detalle_orden')
        else:
            form = DetalleOrdenForm()

        return render(request, 'crear_detalle_orden.html', {'form': form})

#=========================================================================================================================
def guardar_datos(request):
    if request.method == 'POST':
        numero_filas = int(request.POST.get('numero_filas'))
        
        for i in range(numero_filas):
            producto = request.POST.get(f'producto_{i}')
            cantidad = request.POST.get(f'cantidad_{i}')
            orden = request.POST.get(f'orden_{i}')
            
            # Guardar los datos en la base de datos (modelo correspondiente)
            # Ejemplo: Crear una nueva instancia y guardarla
            # modelo = MiModelo(nombre=nombre, edad=edad)
            # modelo.save()
        
        return JsonResponse({'mensaje': 'Datos guardados exitosamente'})  # Respuesta JSON de confirmación
        
    return render(request, 'productos/crear_detalle_orden.html') # Si la solicitud no es POST, muestra la página nuevamente
#===========================================================================================================================    

#------------------------------------------------------------------------------------------

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

def Eliminar(request, id):
    Producto=producto.objects.get(id=id)
    Producto.delete()
    return redirect('producto')

#---------------------------------------------------------------------------------------------
