# Generated by Django 3.2.11 on 2022-01-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220127_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passengerinfo',
            name='existed',
        ),
        migrations.AddField(
            model_name='passengerinfo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
