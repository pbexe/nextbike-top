from django.core.management.base import BaseCommand, CommandError
from top.models import Bike, Bike_position, Location
import requests
from django.conf import settings
import json
from pprint import pprint


class Command(BaseCommand):
    help = 'Pulls new data from nextbike'

    def save_bike_info(bike_json):
        if not Bike.filter(number=bike_json["bike_numbers"][0]).exists():
            bike = Bike(number=bike_json["bike_numbers"][0], name=bike_json["name"], ebike=bool(bike_json["bike_list"][0]["battery_pack"]))
            bike.save()
        bike = Bike.objects.get(number=bike_json["bike_numbers"][0])
        pos = Bike_position(bike=bike, lat=float(bike_json["lat"]), long=float(bike_json["lng"]))
        pos.save()


    def handle(self, *args, **options):

        try:
            city=Location(area_id=476, name='Cardiff')
            city.save()
        except Exception as e:
            self.stdout.write(self.style.ERROR(e.__str__()))

        city = Location.objects.all()[0]

        data = requests.get(settings.API_ROOT, params={
            "city": city.area_id
        }).json()["countries"][0]["cities"][0]["places"]

        self.stdout.write(self.style.SUCCESS('Successfully run the pull command'))

        for bike in data:
            if bike["bike"] == True:

                save_bike_info(bike)

                # self.stdout.write(self.style.NOTICE(bike["name"]))
                # pprint(bike)
                
        self.stdout.write(self.style.WARNING('This has not actually been built yet'))
