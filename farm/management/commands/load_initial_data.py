from django.core.management.base import BaseCommand
from farm.models import Farm, Sheep, Pig, Cow


class Command(BaseCommand):
    help = "Load initial data into the database"

    def handle(self, *args, **kwargs):
        # Create Farms
        farm1 = Farm.objects.create(name="Happy Acres")
        farm2 = Farm.objects.create(name="Sunny Meadows")

        # Create Animals
        Sheep.objects.create(farm=farm1, name="Dolly", wool_color="White")
        Sheep.objects.create(farm=farm1, name="Shaun", wool_color="Black")
        Pig.objects.create(farm=farm2, name="Piglet", weight=50)
        Pig.objects.create(farm=farm2, name="Ham", weight=100)
        Cow.objects.create(farm=farm1, name="Daisy", milk_yield=15.0)
        Cow.objects.create(farm=farm2, name="Bessie", milk_yield=20.0)

        self.stdout.write(self.style.SUCCESS("Successfully loaded initial data"))
