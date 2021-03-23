from django.db import models
from django.db.models.fields import BooleanField

class Location(models.Model):
    area_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Bike(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField(blank=False)
    ebike = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Bike_position(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)

