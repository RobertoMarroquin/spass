# Generated by Django 3.2.5 on 2021-12-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0023_alter_indicador_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='nombre',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Nombre'),
        ),
    ]