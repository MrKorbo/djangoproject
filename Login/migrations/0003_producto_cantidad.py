# Generated by Django 4.2.5 on 2023-09-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]