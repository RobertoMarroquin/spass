# Generated by Django 3.2.5 on 2021-09-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0016_auto_20210922_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='mostrar',
            field=models.BooleanField(default=False, verbose_name='Mostrar indicador'),
        ),
    ]
