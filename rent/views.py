from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
from . import models
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "index.html")

@login_required
def home(request, number=0):
    return render(request, "home.html")


#CUSTOMER SECTION:
def customers(request):

    customer_list = models.Customer.objects.all().order_by('last_name')

    customer_list_dict = {
        'customers': customer_list
    }

    return render(request, "customers.html", customer_list_dict)


def customer(request, id):
    customer = models.Customer.objects.get(id=id)
    return render(request, "customer_details.html", {'customer':customer})

@login_required
def add_newcustomer(request):

    if request.method == 'POST':

        form = forms.AddCustomer(request.POST)
        if form.is_valid():
            customer = models.Customer(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                address=form.cleaned_data["address"],
                city=form.cleaned_data["city"],
                country=form.cleaned_data["country"],
            )
            customer.save()
        return redirect('customers')

    else:
        form = forms.AddCustomer
        return render(request, "add_newcustomer.html", {'form': form})


#RENTALS SECTION

@login_required
def rentals(request):

    list_of_rentals = models.Rental.objects.all().order_by('return_date')

    rental_list_dict = {
    'rentals': list_of_rentals
    }

    return render(request, "rentals.html", rental_list_dict)

def rentalbooking(request, id):
    rental = models.Rental.objects.get(id=id)
    return render(request, "rentalbooking_details.html", {'rental':rental})


@login_required
def make_newrentalbooking(request):

    if request.method == 'POST':

        form = forms.NewRentalBooking(request.POST)
        if form.is_valid():
            rental = models.Rental(
                rental_date=form.cleaned_data["rental_date"],
                return_date=form.cleaned_data["return_date"],
                customer=form.cleaned_data["customer"], ##ask foriegn key
                vehicle=form.cleaned_data["vehicle"], ##ask foriegn key
                )
            rental.save()
        return redirect('rentals')

    else:
        form = forms.NewRentalBooking
        return render(request, "book_rental.html", {'form': form})



# Vehicle SECTION:
def vehicles(request):
    vehicles_list = models.Vehicle.objects.all().order_by('date_created')

    vehicle_list_dict = {
        'vehicles': vehicles_list
    }

    return render(request, "vehicles.html", vehicle_list_dict)


def vehicle(request, id):
    vehicle = models.Vehicle.objects.get(id=id)
    return render(request, "vehicle_details.html", {'vehicle': vehicle})

@login_required
def add_newvehicle(request):
    if request.method == 'POST':

        form = forms.AddVehicle(request.POST)
        if form.is_valid():
            vehicle = models.Vehicle(
                vehicle_type=form.cleaned_data["vehicle_type"],
                date_created=form.cleaned_data["date_created"],
                real_cost=form.cleaned_data["real_cost"],
                size=form.cleaned_data["size"],
            )
            vehicle.save()
        return redirect('vehicles')

    else:
        form = forms.AddVehicle
        return render(request, "add_newVehicle.html", {'form': form})

# for sign up form

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})