# Generated by Django 4.1.1 on 2022-09-29 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paquetes', '0004_location_municipio_alter_location_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='municipio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paquetes.municipio'),
        ),
    ]
