# Generated by Django 3.0.2 on 2020-05-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='device_serial',
            field=models.CharField(max_length=50),
        ),
    ]
