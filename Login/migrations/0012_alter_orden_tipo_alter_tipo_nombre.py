# Generated by Django 4.2.5 on 2023-09-27 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0011_alter_orden_receptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.tipo'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]