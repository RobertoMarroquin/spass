# Generated by Django 3.2.5 on 2021-11-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0020_auto_20211028_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='descripcion',
            field=models.CharField(default=None, max_length=300, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
