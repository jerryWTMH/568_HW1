from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
TYPE_CHOICES = {('SUV', 'SUV'), ('COMPACT', 'COMPACT'), ('SEDAN', 'SEDAN')}

class PassengerInfo(models.Model):
    date_posted = models.DateTimeField(auto_now = True)
    address = models.CharField(max_length = 50)
    arrival_time = models.CharField(max_length = 50, help_text = 'Format:2022-01-24 12:00')
    party_number = models.IntegerField(default = 1)
    vehicle_type = models.CharField(max_length = 15, choices = TYPE_CHOICES, default= 'COMPACT')
    sharing_ride = models.BooleanField(default = False)
    special_request = models.TextField(null= True, blank = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    confirmed = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)
    driver = models.CharField(default ='', blank = True, max_length = 50)
    sharers = ArrayField(
        models.CharField(max_length = 50, blank = True, null = True),
        blank = True, default = list
    )



    def _str_(self):
        return "At " + self.address
class DriverInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    driver_license = models.CharField(max_length = 19, default = '', blank = True)
    capacity = models.PositiveIntegerField(default = 0)
    vehicle_type = models.CharField(max_length = 15, choices = TYPE_CHOICES, default = 'COMPACT')
    vehicle_model_make = models.CharField(default = '', max_length = 150)
    my_request = models.IntegerField(default = -1)
    passenger = models.CharField(default = '', blank = True, max_length = 50)

    def _str_(self):
        return f'{self.user.username} DriverInfo'
    


