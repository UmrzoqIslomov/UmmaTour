# Generated by Django 3.2.13 on 2022-12-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umravaxajapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='adress',
            field=models.CharField(max_length=128),
        ),
    ]