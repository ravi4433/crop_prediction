from django import forms
from multiselectfield import MultiSelectFormField
class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your name'
            }
        )
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
            }
        )
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your City'
            }
        )
    )
    mobile = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Mobile Number'
            }
        )
    )
    query = forms.CharField(
        label="",
        widget= forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Feedback Here or Any Query'
            }
        )
    )

class Crops(forms.Form):
    LOCATION_CHOICES = (
        ('Banda','Banda'),
        ('Lucknow', 'Lucknow'),
        ('Siddharth nagar', 'Siddharth nagar'),
        ('Pryagraj', 'Pryagraj'),
        ('Chitrakoot', 'Chitrakoot'),
        ('Jhansi', 'Jhansi'),
        ('Bulandshahar', 'Bulandshahar'),
        ('Kanpur', 'Kanpur'),
        ('Meerut', 'Meerut'),
        ('Agra', 'Agra'),
        ('Gorakhpur', 'Gorakhpur'),
        ('Maharajganj', 'Maharajganj'),
        ('Santkabir nagar', 'Santkabir nagar'),
        ('Saharanpur', 'Saharanpur'),
        ('Balrampur', 'Balrampur'),
        ('Gonda', 'Gonda'),
        ('Basti', 'Basti'),
        ('Balia', 'Balia'),
        ('Banaras', 'Banaras'),
        ('Jaunpur', 'Jaunpur'),
        ('Sobhadra', 'Sonbhadra')
    )
    location = forms.CharField(
        label="City",
        widget=forms.Select(
            choices=LOCATION_CHOICES,
            attrs={
                'class': 'form-control'
            }
        )
    )
    SOIL_CHOICES= (

        ('Red','Red'),
        ('Brown', 'Brown'),
        ('Allubial', 'Allubial'),
        ('Rock', 'Rock'),
        ('Black', 'Black'),
        ('Latterite', 'Latterite')
    )
    soil_type = forms.CharField(
        label="Soil_Type",
        widget= forms.Select(
            choices=SOIL_CHOICES,
            attrs={
                'class': 'form-control'
            }
        )
    )
    MONTH_CHOICES = (
        ('Jan', 'JAN'),
        ('Feb', 'FEB'),
        ('Mar', 'MAR'),
        ('Apr', 'APR'),
        ('May', 'MAY'),
        ('Jun', 'JUN'),
        ('Jul', 'JUL'),
        ('Aug', 'AUG'),
        ('Sep', 'SEP'),
        ('Oct', 'OCT'),
        ('Nov', 'NOV'),
        ('Dec', 'DEC')
    )
    month = forms.CharField(
        label="Month",
        widget=forms.Select(
            choices=MONTH_CHOICES,
            attrs={
                'class': 'form-control'
            }
        )
    )