# Generated by Django 4.2 on 2023-05-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0002_carreto_nomcarreto_alter_carreto_idcarreto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreto',
            name='idCarreto',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
