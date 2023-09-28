from django import forms
from .models import producto, detalle_orden

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ('__all__')

class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = detalle_orden
        fields = ['cantidad', 'producto', 'orden']
