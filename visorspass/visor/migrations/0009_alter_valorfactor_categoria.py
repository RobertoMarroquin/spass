# Generated by Django 3.2.5 on 2021-08-25 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0008_alter_indicador_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valorfactor',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='valores', to='visor.factordesagregacion'),
        ),
    ]
