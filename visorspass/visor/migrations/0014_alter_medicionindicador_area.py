# Generated by Django 3.2.5 on 2021-09-14 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0013_medicionindicador_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicionindicador',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicadores', to='visor.area'),
        ),
    ]
