from faker import Faker
from rent.models import Customer, Vehicle_type, Vehicle_size, Vehicle, Rental, Rental_rate
from datetime import timedelta    #this makes it possible to add days to a previous saved date
from random import randint

#create objects to input data in tables

faker = Faker()


#Fill the Customer table with some fake data using Faker
# create instances for Customer :


for i in range(100):
    customer= Customer(first_name= faker.first_name(), last_name= faker.last_name(), email= faker.email(), phone_number=faker.phone_number(), address= faker.address(), city = faker.city(), country= faker.country())
    customer.save() #find way to connect to database manually so to run it in this py file


# Create a few vehicle types in the database (‘bike’, ‘electric bike’, ‘scooter’, ‘jetpack’, etc.)
# create instances for Vehicle Type :
bike = Vehicle_type(name= 'Bike')
ebike = Vehicle_type(name= 'Electric Bike')
quadbike = Vehicle_type(name= 'Quad Bike')
dirtbike = Vehicle_type(name= 'Dirt Bike')
motorbike = Vehicle_type(name= 'Motor Bike')
scooter = Vehicle_type(name= 'Scooter')
jamesbond =Vehicle_type(name= 'HMS James Bond Motor Bike')
snowmobile = Vehicle_type(name= 'Snow Mobile')
terminatorsbike = Vehicle_type(name= 'Terminators Bike')
batmans = Vehicle_type(name= 'Batmans Bike')
ghost = Vehicle_type(name= 'Ghost Riders Bike')

types =[bike, ebike, quadbike, dirtbike, motorbike, scooter, jamesbond, snowmobile, terminatorsbike, batmans, ghost]
for type in types:
    type.save()




# Create a few vehicle sizes - ‘small’, ‘medium’, ‘large’, ‘double’, etc.
# # create instances for Vehicle size :
vsmall= Vehicle_size(name= 'Very Small')
small= Vehicle_size(name= 'Small')
medium= Vehicle_size(name= 'Medium')
Big= Vehicle_size(name= 'Big')
vbig= Vehicle_size(name= 'Very Big')

sizes =[vsmall, small, medium, Big, vbig]
for size in sizes:
    size.save()

# Create a few vehicles-
# # create instances for Vehicle:

def rand_date():
    created_date = faker.date_between(start_date="-5y", end_date="-3y")
    return created_date

bike = Vehicle(vehicle_type=Vehicle_type.objects.get(name="Bike"), date_created= rand_date(), real_cost=100, size=Vehicle_size.objects.get(name="Very Small"))
ebike = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Electric Bike"), date_created= rand_date(), real_cost=250, size= Vehicle_size.objects.get(name="Small"))
quadbike = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Quad Bike"), date_created= rand_date(), real_cost=700, size= Vehicle_size.objects.get(name="Big"))
dirtbike = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Dirt Bike"), date_created= rand_date(), real_cost=500, size= Vehicle_size.objects.get(name="Small"))
motorbike = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Motor Bike"), date_created= rand_date(), real_cost=600, size= Vehicle_size.objects.get(name="Medium"))
scooter = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Scooter"), date_created= rand_date(), real_cost=550, size= Vehicle_size.objects.get(name="Small"))
jamesbond =Vehicle(vehicle_type=Vehicle_type.objects.get(name="HMS James Bond Motor Bike"), date_created= rand_date(), real_cost=10000, size= Vehicle_size.objects.get(name="Medium"))
snowmobile = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Snow Mobile"), date_created= rand_date(), real_cost=1200, size= Vehicle_size.objects.get(name="Very Big"))
terminatorsbike = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Terminators Bike"), date_created= rand_date(), real_cost=676, size= Vehicle_size.objects.get(name="Medium"))
batmans = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Batmans Bike"), date_created= rand_date(), real_cost=300000, size=Vehicle_size.objects.get(name="Very Big"))
ghost = Vehicle(vehicle_type= Vehicle_type.objects.get(name="Ghost Riders Bike"), date_created= rand_date(), real_cost=666, size= Vehicle_size.objects.get(name="Big"))

vehs =[bike, ebike, quadbike, dirtbike, motorbike, scooter, jamesbond, snowmobile, terminatorsbike, batmans, ghost]
for veh in vehs:
    veh.save()


# class Vehicle(models.Model):
#
#     vehicle_type=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
#     date_created= models.DateField()
#     real_cost = models.FloatField()
#     size= models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)


# Create a few rentals-
# # create instances for Rental:

# Customer.objects.get(id=randint(1,100)).id - get specific id of a random customer choosing him/her by id

for i in range(300):
    my_rental_date = faker.date_between(start_date="-3y", end_date="today")
    my_return_date = my_rental_date + timedelta(days=randint(1, 15))
    rentalbooking= Rental(rental_date= my_rental_date, return_date= my_return_date, customer=Customer.objects.get(id=randint(1,100)).id, vehicle=Vehicle.objects.get(id=randint(1,11)).id)
    rentalbooking.save() #find way to connect to database manually so to run it in this py file

# class Rental(models.Model):
#
#     rental_date = models.DateField()
#     return_date = models.DateField(null=True) #return date can  sometimes be null
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


# Create a few rental rates-
# # create instances for Rental_rate:


bike = Rental_rate(daily_rate= 50, vehicle_type= Vehicle_type.objects.get(name="Bike"), vehicle_size= Vehicle_size.objects.get(name="Very Small"))
ebike = Rental_rate(daily_rate=100, vehicle_type= Vehicle_type.objects.get(name="Electric Bike"), vehicle_size= Vehicle_size.objects.get(name="Small"))
quadbike = Rental_rate(daily_rate=350, vehicle_type= Vehicle_type.objects.get(name="Quad Bike"), vehicle_size= Vehicle_size.objects.get(name="Big"))
dirtbike = Rental_rate(daily_rate= 250, vehicle_type= Vehicle_type.objects.get(name="Dirt Bike"), vehicle_size= Vehicle_size.objects.get(name="Small"))
motorbike = Rental_rate(daily_rate= 300, vehicle_type= Vehicle_type.objects.get(name="Motor Bike"), vehicle_size= Vehicle_size.objects.get(name="Medium"))
scooter = Rental_rate(daily_rate= 275, vehicle_type= Vehicle_type.objects.get(name="Scooter"), vehicle_size= Vehicle_size.objects.get(name="Small"))
jamesbond =Rental_rate(daily_rate= 5000, vehicle_type= Vehicle_type.objects.get(name="HMS James Bond Motor Bike"), vehicle_size= Vehicle_size.objects.get(name="Medium"))
snowmobile = Rental_rate(daily_rate= 500, vehicle_type= Vehicle_type.objects.get(name="Snow Mobile"), vehicle_size= Vehicle_size.objects.get(name="Very Big"))
terminatorsbike = Rental_rate(daily_rate= 350, vehicle_type= Vehicle_type.objects.get(name="Terminators Bike"), vehicle_size= Vehicle_size.objects.get(name="Medium"))
batmans = Rental_rate(daily_rate=100000, vehicle_type= Vehicle_type.objects.get(name="Batmans Bike"), vehicle_size= Vehicle_size.objects.get(name="Very Big"))
ghost = Rental_rate(daily_rate=333, vehicle_type= Vehicle_type.objects.get(name="Ghost Riders Bike"), vehicle_size= Vehicle_size.objects.get(name="Big"))

vehiclesrate =[bike, ebike, quadbike, dirtbike, motorbike, scooter, jamesbond, snowmobile, terminatorsbike, batmans, ghost]
for vehr in vehiclesrate:
    vehr.save()


# class Rental_rate(models.Model):   #how to add this in the same view for vehicle details
#     daily_rate = models.FloatField()
#     vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
#     vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)
#


