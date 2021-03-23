from django.shortcuts import render, HttpResponse
from .models import Bike, Bike_position, Location
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

def home(request):
    payload = ""
    bikes = get_list_or_404(Bike)
    for bike in bikes:
        payload += '<a href="/bike/' + str(bike.number) + '">' + bike.name + '</a>' + '<br>'
    return HttpResponse(payload)

def bike(request, number):
    bike = get_object_or_404(Bike, number=number)
    locations = get_list_or_404(Bike_position, bike=bike)
    payload = "Locations for " + bike.name + "<br>"
    for location in locations:
        payload += str(location)
        payload += "<br>"
    return HttpResponse(payload)