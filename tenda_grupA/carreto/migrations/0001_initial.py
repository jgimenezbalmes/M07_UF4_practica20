# Generated by Django 4.2 on 2023-04-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cataleg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreto',
            fields=[
                ('idCarreto', models.IntegerField(primary_key=True, serialize=False)),
                ('productes', models.ManyToManyField(to='cataleg.producte')),
            ],
        ),
    ]
