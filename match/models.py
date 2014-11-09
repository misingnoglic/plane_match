from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Flight(models.Model):
    number = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    origin = models.CharField(max_length=10)
    #departure = models.DateTimeField()

    def __str__(self):
        return str(self.number)
    #participants = models.ManyToManyField(AirlineUser)

class Seat(models.Model):
    number = models.CharField(max_length=4)
    flight = models.ForeignKey(Flight)
    def __str__(self):
        return str(self.number)

class Interest(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)

class Hotel(models.Model):
    name = models.CharField(max_length=10)
    #guests = models.ManyToManyField(user)
    def __str__(self):
        return str(self.name)

class AirlineUser(models.Model):
    #friends_made = 0
    user = models.OneToOneField(User)
    interests = models.ManyToManyField(Interest, blank=True)
    def __str__(self):
        return str(self.user.username)


class PersonOnFlight(models.Model):
    person = models.ForeignKey(AirlineUser)
    hotel = models.ForeignKey(Hotel, blank=True)
    flight = models.ForeignKey(Flight, blank=True)
    def __str__(self):
        return str(self.person.user.username)
