# Generated by Django 3.2.11 on 2022-01-25 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=50)),
                ('arrival_time', models.CharField(help_text='Format:2022-01-24 12:00', max_length=50)),
                ('party_number', models.IntegerField(default=1)),
                ('vehicle_type', models.CharField(choices=[('SEDAN', 'SEDAN'), ('COMPACT', 'COMPACT'), ('SUV', 'SUV')], default='COMPACT', max_length=15)),
                ('sharing_ride', models.BooleanField(default=False)),
                ('special_request', models.TextField(blank=True, null=True)),
                ('existed', models.BooleanField(default=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('driver', models.CharField(blank=True, default='', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_license', models.CharField(blank=True, default='', max_length=19)),
                ('max_passengers', models.PositiveIntegerField(default=0)),
                ('vehicle_Type', models.CharField(choices=[('SEDAN', 'SEDAN'), ('COMPACT', 'COMPACT'), ('SUV', 'SUV')], default='COMPACT', max_length=15)),
                ('vehicle_Model_Make', models.CharField(default='', max_length=150)),
                ('my_request', models.IntegerField(default=-1)),
                ('passenger', models.CharField(blank=True, default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
