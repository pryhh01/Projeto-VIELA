# Generated by Django 4.1 on 2022-08-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='senha',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
    ]