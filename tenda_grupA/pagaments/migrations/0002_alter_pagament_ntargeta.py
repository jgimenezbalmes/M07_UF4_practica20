# Generated by Django 4.2 on 2023-05-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagament',
            name='nTargeta',
            field=models.BigIntegerField(),
        ),
    ]
