from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Flight(models.Model):
    number = models.CharField(max_length=10)
    #participants = models.ManyToManyField(AirlineUser)

class Seat(models.Model):
    number = models.CharField(max_length=4)
    flight = models.ForeignKey(Flight)


class Hobby(models.Model):
    name = models.CharField(max_length=10)

class Category(models.Model):
    name = models.CharField(max_length=10)

class Hotel(models.Model):
    name = models.CharField(max_length=10)
    #guests = models.ManyToManyField(user)

class AirlineUser(models.Model):
    #friends_made = 0
    user = models.ForeignKey(User)
    hobbies = models.ManyToManyField(Category)


class PersonOnFlight(models.Model):
    person = models.ForeignKey(AirlineUser)
    hotel = models.ForeignKey(Hotel)
    flight = models.ForeignKey(Flight)
