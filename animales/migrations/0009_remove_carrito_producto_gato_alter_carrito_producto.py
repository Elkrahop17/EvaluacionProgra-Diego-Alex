# Generated by Django 5.0.6 on 2024-06-25 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0008_alter_carrito_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='producto_gato',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.animalproducto'),
        ),
    ]
