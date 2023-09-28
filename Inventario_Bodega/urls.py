from django.contrib import admin
from django.urls import path, include
from Login import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('inicio/', include('Login.urls')),
    path('', views.Login.as_view(), name='login'),
    path('inicio', views.Inicio.as_view(), name='inicio'),
]
