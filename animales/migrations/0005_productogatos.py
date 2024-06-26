# Generated by Django 5.0.6 on 2024-06-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0004_productoperros'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoGatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('minutos', models.IntegerField(default=0)),
            ],
        ),
    ]
