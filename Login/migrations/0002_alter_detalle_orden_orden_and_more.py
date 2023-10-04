# Generated by Django 4.2.5 on 2023-10-04 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_orden',
            name='orden',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.orden'),
        ),
        migrations.AlterField(
            model_name='detalle_orden',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Login.categoria'),
        ),
    ]