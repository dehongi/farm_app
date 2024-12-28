from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=255)


class Animal(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="animals")
    name = models.CharField(max_length=255)


class Sheep(Animal):
    wool_color = models.CharField(max_length=50)


class Pig(Animal):
    weight = models.IntegerField()


class Cow(Animal):
    milk_yield = models.FloatField()
