# Generated by Django 3.2.4 on 2021-06-13 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGeekapp', '0005_rename_title_comentario_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='Nombre_sala',
            new_name='Nombre_juego',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='description',
        ),
    ]
