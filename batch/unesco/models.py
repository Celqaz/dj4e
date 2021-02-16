from django.db import models


# name,description,justification,
# year,longitude,latitude, area_hectares,
# category,states,region,iso

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    justification = models.CharField(max_length=1024)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)

    # one to many
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# one to many
class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(null=True, max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.name
