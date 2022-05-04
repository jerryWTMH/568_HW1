# Generated by Django 4.0.1 on 2022-01-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_driverinfo_vehicle_type_alter_passengerinfo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverinfo',
            name='vehicle_type',
            field=models.CharField(choices=[('SEDAN', 'SEDAN'), ('COMPACT', 'COMPACT'), ('SUV', 'SUV')], default='COMPACT', max_length=15),
        ),
        migrations.AlterField(
            model_name='passengerinfo',
            name='vehicle_type',
            field=models.CharField(choices=[('SEDAN', 'SEDAN'), ('COMPACT', 'COMPACT'), ('SUV', 'SUV')], default='COMPACT', max_length=15),
        ),
    ]