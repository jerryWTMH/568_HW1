# Generated by Django 3.2.11 on 2022-01-25 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=50)),
                ('arrival_time', models.CharField(help_text='Format:2022-01-24 12:00', max_length=50)),
                ('party_number', models.IntegerField(default=1)),
                ('vehicle_type', models.CharField(choices=[('COMPACT', 'COMPACT'), ('SEDAN', 'SEDAN'), ('SUV', 'SUV')], default='COMPACT', max_length=15)),
                ('sharing_ride', models.BooleanField(default=False)),
                ('special_request', models.TextField(blank=True, null=True)),
                ('existed', models.BooleanField(default=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('driver', models.CharField(blank=True, default='', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='driverinfo',
            name='vehicle_Type',
            field=models.CharField(choices=[('COMPACT', 'COMPACT'), ('SEDAN', 'SEDAN'), ('SUV', 'SUV')], default='COMPACT', max_length=15),
        ),
        migrations.DeleteModel(
            name='RideRequest',
        ),
    ]
