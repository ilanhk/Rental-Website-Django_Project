from django.contrib.admin import options
from django.db import models

# Create your models here.

#create customer

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __repr__(self):      #dont really understand the point of repr????
        return f"Customer: {self.first_name} {self.last_name}"

class Vehicle_type(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return f"Vehicle Type: {self.name}"

class Vehicle_size(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return f"Vehicle Size: {self.name}"

class Vehicle(models.Model):

    vehicle_type=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    date_created= models.DateField()
    real_cost = models.FloatField()
    size= models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Vehicle: {self.vehicle_type} {self.date_created} {self.real_cost} {self.size}"


class Rental(models.Model):

    rental_date = models.DateField()
    return_date = models.DateField(null=True) #return date can  sometimes be null
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Rental: {self.customer} {self.vehicle} {self.rental_date} {self.return_date}"

class Rental_rate(models.Model):   #how to add this in the same view for vehicle details
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Rental Rate:: {self.vehicle_type} {self.vehicle_size} {self.daily_rate}"

