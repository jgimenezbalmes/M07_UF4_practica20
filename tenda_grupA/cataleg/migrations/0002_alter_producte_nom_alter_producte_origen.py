# Generated by Django 4.2 on 2023-04-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cataleg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producte',
            name='nom',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='producte',
            name='origen',
            field=models.CharField(max_length=50, verbose_name='origen'),
        ),
    ]
