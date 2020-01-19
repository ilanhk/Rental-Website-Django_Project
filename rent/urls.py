from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #the name section (called reverse) use in the settings , b4 is what you type in url
    path('home/', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('customer_details/<int:id>', views.customer, name='customer_details'),
    path('add_newcustomer/', views.add_newcustomer, name='add_newcustomer'),
    path('rentals/', views.rentals, name='rentals'),
    path('rental_details/<int:id>', views.rentalbooking, name='rental_details'),
    path('book_rental/', views.make_newrentalbooking, name='book_rental'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicle_details/<int:id>', views.vehicle, name='vehicle_details'),
    path('add_newvehicle/', views.add_newvehicle, name='add_newvehicle'),
    path('signup/', views.signup, name='sign'),

]
