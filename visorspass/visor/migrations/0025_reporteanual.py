# Generated by Django 3.2.5 on 2022-02-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0024_alter_indicador_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteAnual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('anyo', models.IntegerField(verbose_name='Año')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Reporte Anual',
                'verbose_name_plural': 'Reportes Anuales',
            },
        ),
    ]
