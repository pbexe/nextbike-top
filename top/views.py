from django.shortcuts import render, HttpResponse
from .models import Bike
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.

def home(request):
    return HttpResponse("hello")

def bike(request, number):
    bike = get_object_or_404(Bike, number=number)
    return HttpResponse(bike.name)