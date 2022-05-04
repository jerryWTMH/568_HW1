from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django import forms
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


from main.forms import DriverUpdateForm, PassengerUpdateForm, UserRegisterForm, SearchForm, DriveSearchForm
from .models import PassengerInfo, DriverInfo
from django.views.generic import CreateView
from django.contrib.auth.models import User



#from django.urls import reverse_lazy

# Create your views here.
def homepage(request):
    return render(request, 'main/home.html')
def mainpage(request):
    
    try:
        driver = DriverInfo.objects.get(user = request.user.id)
    except ObjectDoesNotExist:
        driver = None
    context = {
        'driver': driver
    }
    return render(request, 'main/mainpage.html', context)
def request_ride(request):
    return HttpResponse("This will link to database!")

def join_ride(request):
    # sharer = PassengerInfo.object.filter(sh)
    return render(request, 'main/join_ride.html')

def share_detail(request, pk):
    passenger = PassengerInfo.objects.get(id = pk)
    passenger.party_number += 1
    passenger.sharers.append(request.user.username)
    passenger.save()
    if passenger.driver != "": 
        driver = DriverInfo.objects.get(user = str(passenger.driver)) ## check driver passing type! 
    else:
        driver = ""
    context= {
        'request':PassengerInfo.objects.get(id = pk),
        'driver': driver
    }
    return render(request, 'main/share_detail.html', context) ## check driver passing type!

def ride_info(request): 
    passenger = PassengerInfo.objects.filter(owner_id = request.user.id)
    orders = PassengerInfo.objects.filter(sharing_ride = True).exclude(owner_id = request.user.id).filter(sharers__contains =[request.user.username])
    passenger = passenger.union(orders)
    # for order in orders:
    #     if(request.user.username in order.sharers):
    #         passenger = passenger.union(order)
    # for order in orders:  
    #     if request.user.username in order.sharers:
            

    context = {'requests':passenger}
    return render(request, 'main/ride_info.html',context)
    #return HttpResponse(passenger.vehicle_type)
    # return render(request, 'main/ride_info.html')

# def edit_passenger(request):    
#     if request.method == 'POST':
#         # passenger = get_object_or_404(PassengerInfo,  _id=request.user.id)
#         passengers = PassengerInfo.objects.filter(owner_id = request.user.id) & PassengerInfo.objects.filter(confirmed = False)
#         forms=[]
#         for passenger in passengers:
#             form = PassengerUpdateForm(request.POST)
#             if form.is_valid():
#                 passenger.address = form.cleaned_data['address']
#                 passenger.arrival_time = form.cleaned_data['arrival_time']
#                 passenger.party_number = form.cleaned_data['party_number']
#                 passenger.vehicle_type = form.cleaned_data['vehicle_type']
#                 passenger.sharing_ride = form.cleaned_data['sharing_ride']
#                 passenger.special_request = form.cleaned_data['special_request']
#                 passenger.save()              
#                 forms.append(form)
#                 break
#                 # return HttpResponseRedirect(reverse('mainpage'))
#     else:
#         passengers = PassengerInfo.objects.filter(owner_id = request.user.id) & PassengerInfo.objects.filter(confirmed = False)
#         forms=[]
#         for passenger in passengers:
#             form = PassengerUpdateForm(initial = {
#                 'address':passenger.address,
#                 'arrival_time':passenger.arrival_time,
#                 'party_number':passenger.party_number,
#                 'vehicle_type' : passenger.vehicle_type,
#                 'sharing_ride':passenger.sharing_ride,
#                 'special_request':passenger.special_request,
#             })
#             forms.append(form)
#     context = {
#         'forms':forms,
#     }
#     return render(request, 'main/edit_passenger.html',context)

def edit_passenger(request, pk):    
    if request.method == 'POST':
        # passenger = get_object_or_404(PassengerInfo,  _id=request.user.id)
        #& PassengerInfo.objects.filter(id = pk)
        #passengers = PassengerInfo.objects.filter(owner_id = request.user.id) 
        passengers = PassengerInfo.objects.get(id = pk) 
        #forms=[]
        #for passenger in passengers:
        form = PassengerUpdateForm(request.POST)
        if form.is_valid():
            passengers.address = form.cleaned_data['address']
            passengers.arrival_time = form.cleaned_data['arrival_time']
            passengers.party_number = form.cleaned_data['party_number']
            passengers.vehicle_type = form.cleaned_data['vehicle_type']
            passengers.sharing_ride = form.cleaned_data['sharing_ride']
            passengers.special_request = form.cleaned_data['special_request']
            passengers.save()              
            #forms.append(form)
                
        return HttpResponseRedirect(reverse('mainpage'))
    else:
        #passengers = PassengerInfo.objects.filter(id = pk)
        passengers = PassengerInfo.objects.filter(id = pk)
        forms=[]
        for passenger in passengers:
            form = PassengerUpdateForm(initial = {
                    'address':passenger.address,
                    'arrival_time':passenger.arrival_time,
                    'party_number':passenger.party_number,
                    'vehicle_type' : passenger.vehicle_type,
                    'sharing_ride':passenger.sharing_ride,
                    'special_request':passenger.special_request,
                })
            forms.append(form)
    context = {
        'forms':forms,
    }
    return render(request, 'main/edit_passenger.html',context)

def my_confirmed_ride(request):
    orders = PassengerInfo.objects.filter(owner_id = request.user.id, confirmed =True, completed = False)
    orders2 = PassengerInfo.objects.filter(sharers__contains =[request.user.username]).exclude(completed = True)
    orders = orders.union(orders2)
    context = {'requests': orders}
    return render(request, 'main/my_confirmed_ride.html', context)

    

def go_driver(request):
    open_orders = PassengerInfo.objects.filter(confirmed = False)
    context = {'requests':open_orders}
    return render(request, 'main/go_driver.html', context)
def complete_drive_detail(request, pk):
    passenger = PassengerInfo.objects.get(id = pk)
    passenger.completed = True    
    # if passenger.driver != "": 
    #     driver = DriverInfo.objects.get(user = str(passenger.driver)) ## check driver passing type! 
    # else:
    passenger.driver = request.user.username
    driver = DriverInfo.objects.get(user = request.user.id)
    passenger.save()

    sharers = passenger.sharers
    result = []
    for sharer in sharers:
        person = User.objects.get(username = sharer)
        result.append(person.email)
    result.append((User.objects.get(username = passenger.owner)).email)
    send_mail(
        subject='Completed Drive!', 
        message='Your order is completed! Thank you very much! (netid: ch450 nh185)',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list= result,
    )
    context= {
        'request':PassengerInfo.objects.get(id = pk),
        'driver': driver
    }
    return render(request, 'main/complete_drive_detail.html', context)

def drive_detail(request, pk):
    passenger = PassengerInfo.objects.get(id = pk)
    passenger.confirmed = True    
    # if passenger.driver != "": 
    #     driver = DriverInfo.objects.get(user = str(passenger.driver)) ## check driver passing type! 
    # else:
    passenger.driver = request.user.username
    driver = DriverInfo.objects.get(user = request.user.id)
    passenger.save()
    context= {
        'request':PassengerInfo.objects.get(id = pk),
        'driver': driver
    }
    return render(request, 'main/drive_detail.html', context) ## check driver passing type!
# def edit_driver(request):
#     user = request.user
#     d_form = DriverUpdateForm(request.POST, instance = request.user)
#     if d_form.is_valid():
#         d_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('main/vehicle_info')
#     return render(request, 'main/edit_driver.html')
def edit_driver(request):    
    if request.method == 'POST':
        driver = get_object_or_404(DriverInfo, user=request.user.id)
        form = DriverUpdateForm(request.POST)
        if form.is_valid():
            driver.driver_license = form.cleaned_data['driver_license']
            driver.capacity = form.cleaned_data['capacity']
            driver.vehicle_type = form.cleaned_data['vehicle_type']
            driver.vehicle_model_make = form.cleaned_data['vehicle_model_make']
            driver.my_request = form.cleaned_data['my_request']
            driver.save()
            return HttpResponseRedirect(reverse('mainpage'))
    else:
        if not hasattr(request.user, 'driverinfo'):
            user = DriverInfo.objects.create(user = request.user)
            user.save()
        #form = DriverUpdateForm(instance=request.user.driverinfo)
        driver = get_object_or_404(DriverInfo, user=request.user.id)
        form = DriverUpdateForm(initial = {
            'driver_license':driver.driver_license,
            'capacity':driver.capacity,
            'vehicle_type':driver.vehicle_type,
            'vehicle_model_make' : driver.vehicle_model_make,
            'my_request':driver.my_request,
        })
    context = {
        'form':form,
    }
    return render(request, 'main/edit_driver.html',context)

def driver_reg(request): # temporarily out of order
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        user = request.user
        d_form = DriverUpdateForm(request.POST, instance=request.user)
        if form.is_valid() and d_form.is_valid():
                form.save()
                d_form.save()
                return HttpResponseRedirect(reverse('mainpage'))
    else:
        form = UserCreationForm(instance=request.user)
        if not hasattr(request.user, 'user'):
            user = DriverInfo.objects.create(user = request.user)
        d_form = DriverUpdateForm(instance=request.user)
    context = {
        'form':form,
        'd_form':d_form
    }
    return render(request, 'main/driver_reg.html',context)

def vehicle_info(request):
    driver = DriverInfo.objects.filter(user = request.user.id)
    context = {'requests':driver}
    return render(request, 'main/vehicle_info.html',context)

def user_info(request):
    # u = User.objects.get(request.user.id)
    return HttpResponse(request.user.id)

def test_form(request):
    if request.method == "POST":
        email = request.POST.get('email')
        return HttpResponse(email)
    return render(request, "form.html")

class PassengerInfoView(CreateView):
    model = PassengerInfo
    fields = ['address','arrival_time','vehicle_type','party_number', 'sharing_ride','confirmed','special_request']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('My Ride info')
    template_name = 'main/request_ride.html'

class DriverInfoView(CreateView):
    model = DriverInfo
    fields = ['driver_license','capacity','vehicle_type','vehicle_model_make']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('mainpage')
    template_name = 'main/driver_reg.html'

class RideFilter(BaseFilter):
    search_fields = {
        'search_address' : ['address'],
        'search_passenger_number' : {'operator': '__exact', 'fields': ['party_number']},
        'search_earliest_time' : {'operator' : '__lte', 'fields' : ['arrival_time']},
        'search_latest_time' : {'operator' : '__gte', 'fields':['arrival_time']},
        
    }

class DriveFilter(BaseFilter):
    search_fields = {
        'search_capacity' : {'operator': '__lte', 'fields': ['capacity']},
        'search_vehicle_type' :['vehicle_type'],
        
    }

class JoinRideView(SearchListView):
    model = PassengerInfo
    template_name = "main/join_ride.html"
    form_class = SearchForm
    filter_class = RideFilter

    def get_queryset(self):
        queryset = PassengerInfo.objects.filter(confirmed = False) & PassengerInfo.objects.filter(sharing_ride = True)
        return queryset

class GoDriveView(SearchListView):
    model = PassengerInfo
    template_name = "main/go_driver.html"
    form_class = DriveSearchForm
    filter_class = DriveFilter

    def get_queryset(self):
        queryset = PassengerInfo.objects.filter(confirmed = False)
        return queryset

# class ShowConfirmed(SearchListView):
#     model = PassengerInfo
#     template_name = "main/my_confirmed_ride.html"
#     form_class = DriveSearchForm
#     filter_class = DriveFilter

#     def get_queryset(self):
#         queryset = PassengerInfo.objects.filter(confirmed = True) & PassengerInfo.objects.filter(completed = False)
#         return queryset

class ConfirmToComplete(SearchListView):
    model = PassengerInfo
    template_name = "main/my_confirmed_ride_driver.html"
    form_class = DriveSearchForm
    filter_class = DriveFilter

    def get_queryset(self):
        queryset = PassengerInfo.objects.filter(confirmed = True)  & PassengerInfo.objects.filter(completed = False) &PassengerInfo.objects.filter(driver = self.request.user)
        return queryset

# class EditDriverInfoView(CreateView):
#     model = DriverInfo
#     fields = ['driver_license','capacity','vehicle_type','vehicle_model_make']
#     #driver = DriverInfo.objects.get(user = request.user.id)
#     #context = {'requests':driver}
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#     success_url = reverse_lazy('Go for a drive')
#     template_name = 'main/edit_driver.html'
    #return render(request, 'main/vehicle_info.html',context) 

# def login(request):
#     return render(request, 'main/login.html')

# def login(request):
#     return render(request, 'main/logout.html')

# class SignUpView(CreateView):
#     #form_class = UserCreationForm
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created')
            return redirect('login')
    else:
        form =UserRegisterForm()
    return render(request, 'registration/signup.html', {'form':form})

def index(request):
    return HttpResponse("Hello Bitch.")
