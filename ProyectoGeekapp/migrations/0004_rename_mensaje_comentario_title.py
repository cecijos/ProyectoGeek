# Generated by Django 3.2.4 on 2021-06-12 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGeekapp', '0003_auto_20210612_0823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='Mensaje',
            new_name='title',
        ),
    ]
