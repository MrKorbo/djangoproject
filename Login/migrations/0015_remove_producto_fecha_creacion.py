# Generated by Django 4.2.5 on 2023-09-28 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0014_remove_tipo_nombre_producto_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_creacion',
        ),
    ]