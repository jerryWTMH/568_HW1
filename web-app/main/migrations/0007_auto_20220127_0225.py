# Generated by Django 3.2.11 on 2022-01-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220127_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverinfo',
            name='vehicle_type',
            field=models.CharField(choices=[('SEDAN', 'SEDAN'), ('SUV', 'SUV'), ('COMPACT', 'COMPACT')], default='COMPACT', max_length=15),
        ),
        migrations.AlterField(
            model_name='passengerinfo',
            name='vehicle_type',
            field=models.CharField(choices=[('SEDAN', 'SEDAN'), ('SUV', 'SUV'), ('COMPACT', 'COMPACT')], default='COMPACT', max_length=15),
        ),
    ]
