from django.core.management.base import BaseCommand, CommandError
from top.models import Bike, Bike_position, Location

class Command(BaseCommand):
    help = 'Pulls new data from nextbike'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully run the pull command'))
        self.stdout.write(self.style.WARNING('This has not actually been built yet'))
