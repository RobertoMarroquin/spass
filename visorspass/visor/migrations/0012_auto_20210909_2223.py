# Generated by Django 3.2.5 on 2021-09-09 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0011_medicionindicador_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='latitud',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='area',
            name='longitud',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitud'),
        ),
    ]
