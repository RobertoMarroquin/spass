# Generated by Django 3.2.5 on 2021-09-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0014_alter_medicionindicador_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='usa_area',
            field=models.BooleanField(default=False, verbose_name='Usa Area'),
        ),
        migrations.AlterField(
            model_name='medicionindicador',
            name='valores_factor',
            field=models.ManyToManyField(blank=True, to='visor.ValorFactor'),
        ),
    ]
