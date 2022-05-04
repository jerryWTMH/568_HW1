from django.urls import include, path
from . import views
from .views import  PassengerInfoView, DriverInfoView, JoinRideView, GoDriveView, ConfirmToComplete
#, UpdateRideView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.homepage, name='home'), #for directing 
    #path('request_ride/', views.request_ride, name='Request Ride'), # it will be linked to database
    path('request_ride/', PassengerInfoView.as_view(), name='Request Ride'),
    path('join_ride/', JoinRideView.as_view(), name='Join a Ride'),
    path('share_detail/<pk>', views.share_detail, name='Share Detail'),
    path('ride_info/', views.ride_info, name='My Ride info'),
    # path('edit_passenger/', views.edit_passenger, name='Edit Passenger'),
    path('edit_passenger/<pk>', views.edit_passenger, name='Edit Passenger'),
    #path('my_confirmed_ride/', views.my_confirmed_ride, name='My Confirmed Ride'),
    path('my_confirmed_ride/', views.my_confirmed_ride, name='My Confirmed Ride'),
    path('my_confirmed_ride_driver/', ConfirmToComplete.as_view(), name='My Confirmed Ride Driver'),
    path('go_driver/', GoDriveView.as_view(), name='Go for a drive'),
    path('drive_detail/<pk>',views.drive_detail , name='Drive Detail'),
    path('complete_drive_detail/<pk>',views.complete_drive_detail , name='Complete Drive Detail'),
    path('driver_reg/', DriverInfoView.as_view(), name='Driver registration'),
    path('edit_driver/', views.edit_driver, name='Edit Driver'),
    path('vehicle_info/', views.vehicle_info, name='My vehicle'),
    path('user_info/', views.user_info, name='User info'),
    #path('register', SignUpView.as_view(), name='register'),
    path('register', views.sign_up, name='register'),
    path('mainpage', views.mainpage, name = 'mainpage'), # real mainpage
    path ('form/', views.test_form, name="form")
]