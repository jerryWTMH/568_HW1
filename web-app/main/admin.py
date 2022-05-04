from ast import Pass
from django.contrib import admin
from .models import PassengerInfo, DriverInfo
# Register your models here.
admin.site.register(PassengerInfo)
admin.site.register(DriverInfo)
