# Generated by Django 4.2.5 on 2023-09-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_producto_stock_alter_orden_receptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]