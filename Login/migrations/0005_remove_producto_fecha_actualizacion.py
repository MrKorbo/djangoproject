# Generated by Django 4.2.5 on 2023-09-27 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_producto_fecha_actualizacion_producto_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_actualizacion',
        ),
    ]