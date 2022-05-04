from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DriverInfo, PassengerInfo


TYPE_CHOICES = {('SUV', 'SUV'), ('COMPACT', 'COMPACT'), ('SEDAN', 'SEDAN')}

# class request_form(forms.Form):
#     date_posted = forms.DateTimeField()
#     arrival_time = forms.CharField(max_length = 50)
#     vehicle_type = forms.CharField(max_length = 15, choices = TYPE_CHOICES, default= 'COMPACT')
#     sharing_ride = forms.BooleanField(default = False)
#     special_request = forms.ChartField(null= True, blank = True, widget = forms.Textarea)
#     existed = forms.BooleanField(default = True)
#     confirmed = forms.BooleanField(default = False)

class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = ['driver_license','capacity','vehicle_type','vehicle_model_make', 'my_request']

class PassengerUpdateForm(forms.ModelForm):
    class Meta:
        model = PassengerInfo
        fields = ['address','arrival_time','party_number','vehicle_type','sharing_ride','special_request']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class SearchForm(forms.Form):
    search_address = forms.CharField(
        required = False,
        label = 'Search Address',
        widget = forms.TextInput(attrs = {'placeholder':''})
    )
    search_passenger_number = forms.IntegerField(
        required = False,
        label = 'Search Passenger Number:'
    )
    search_latest_time = forms.DateTimeField(
        required = False,
        label='Latest arrival time:'
    )
    search_earliest_time = forms.DateTimeField(
        required = False,
        label = 'Earliest arrival time'
    )

class DriveSearchForm(forms.Form):
    search_capacity= forms.IntegerField(
        required = False,
        label = 'Search Capacity',
    )
    search_vehicle_type = forms.CharField(
        required = False,
        label = 'Vehicle_type'
    )
        

