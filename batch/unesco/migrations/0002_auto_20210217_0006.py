# Generated by Django 3.1.6 on 2021-02-16 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.state'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
