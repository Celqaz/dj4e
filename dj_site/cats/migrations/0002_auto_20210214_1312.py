# Generated by Django 3.1.6 on 2021-02-14 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='foods',
            field=models.CharField(default=0, max_length=300),
        ),
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Breed must be greater than 1 character')]),
        ),
        migrations.AlterField(
            model_name='cat',
            name='nickname',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')]),
        ),
        migrations.AlterField(
            model_name='cat',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
