from django import forms

#CUSTOMER SECTION
class AddCustomer(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control", #form-control is name of css class from bootstrap
            "placeholder": "First Name",
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name",
        })
    )
    email = forms.CharField(          #ask what field to put in
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
        })
    )
    phone_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Phone Number",
        })
    )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Address",
        })
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "City",
        })
    )
    country = forms.CharField(
    max_length = 30,
    widget = forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Country",
    })

    )

#RENTALS SECTION
class NewRentalBooking(forms.Form):
    rental_date= forms.DateField(
            input_formats=['%Y-%m-%d'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control',
                'data-target': '#datepicker1',
                'type': 'date',
            })
        )


    return_date = forms.DateField(
            input_formats=['%Y-%m-%d'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control',
                'data-target': '#datepicker1',
                'type': 'date',
            })
        )
    customer = forms.CharField(                 ##ask foriegn key how to handle?
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Customer",
        })
    )
    vehicle = forms.CharField(                 ##ask
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Vehicle",
        })
    )




#VEHICLES SECTION
class AddVehicle(forms.Form):
    vehicle_type = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Vehicle Type",
        })
    )
    date_created = forms.CharField(  ##can i use datefield??
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Date Created",
        })
    )
    real_cost = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={  ##should i use float???
            "class": "form-control",
            "placeholder": "Real Cost",
        })
    )
    size = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ ##same foriegn key problem
            "class": "form-control",
            "placeholder": "Size",
        })
    )
