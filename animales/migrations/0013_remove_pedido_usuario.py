# Generated by Django 5.0.6 on 2024-06-29 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0012_pedido_pedidoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
    ]
