# Generated by Django 3.2.5 on 2021-08-14 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0005_auto_20210812_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='indicador',
        ),
        migrations.AddField(
            model_name='indicador',
            name='variable',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='indicador', to='visor.variable'),
            preserve_default=False,
        ),
    ]
