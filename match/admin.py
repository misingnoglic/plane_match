from django.contrib import admin
from match.models import Interest, AirlineUser, Flight, PersonOnFlight

admin.site.register(Interest)
admin.site.register(AirlineUser)
admin.site.register(Flight)
admin.site.register(PersonOnFlight)
# Register your models here.

