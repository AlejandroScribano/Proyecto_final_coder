# Generated by Django 3.2.9 on 2022-01-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCentroSalud', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.CharField(max_length=15),
        ),
    ]
