# Generated by Django 4.2 on 2023-05-11 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('carreto', '0003_alter_carreto_idcarreto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreto',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.user'),
        ),
    ]
