# Generated by Django 5.1.2 on 2024-11-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videogames_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videogame',
            old_name='Genre',
            new_name='genre',
        ),
    ]