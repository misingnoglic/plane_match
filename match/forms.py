__author__ = 'arya'
from django import forms
from django.contrib.auth.models import User
from match.models import Interest
from django.contrib.auth.forms import UserCreationForm
from constants import airline_map

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class InterestForm(forms.Form):
    interest = forms.CharField(max_length=20)
    class Meta:
        model = Interest
        fields = ("interest")

class DescriptionForm(forms.Form):
    #Form for putting the description of what you want to do on flight
    description = forms.CharField(widget = forms.Textarea)

class FindFlightForm(forms.Form):
    airlines = airline_map.keys()
    CATEGORY_CHOICES = [    # Note square brackets.
    (1, u'Appetizer'),
    (2, u'Bread'),
    (3, u'Dessert'),
    (4, u'Drinks'),
    (5, u'Main Course'),
    (6, u'Salad'),
    (7, u'Side Dish'),
    (8, u'Soup'),
    (9, u'Sauce/Marinade'),
    (10, u'Other'),
]
    depart_date = forms.DateField
    airline = forms.ChoiceField(choices=CATEGORY_CHOICES)
    origin = forms.CharField(max_length=3)
    destination = forms.CharField(max_length=3)


class FlightNumberForm(forms.Form):
    flight_number = forms.CharField(max_length=5)

class NewFlight(forms.Form):
    class Meta:
        fields = ("from", "to", "date")