from django.db import models

# Create your models here.

class user(models.Model):
    class Estado(models.IntegerChoices):
        Activo = 1
        Inactivo = 2
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    email = models.TextField(null=True)
    password = models.CharField(max_length=16)
    estado = models.IntegerField(choices=Estado.choices)

    def __str__(self):
        fila = "Nombre : " + self.username + " - " + "Email : " + self.email
        return fila

class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=True)
    stock = models.PositiveIntegerField() 

    def __str__(self):
        return self.nombre

class orden(models.Model):
    class tipo_orden(models.IntegerChoices):
        Entrada = 1
        Salida = 2
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    receptor = models.TextField(null=True)
    tipo = models.IntegerField(choices=tipo_orden.choices)
    
class detalle_orden(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField()
    orden = models.PositiveIntegerField()
    producto = models.PositiveIntegerField()