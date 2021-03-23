from django.contrib import admin
from .models import Bike, Bike_position, Location

# Register your models here.

admin.site.register(Bike)
admin.site.register(Bike_position)
admin.site.register(Location)