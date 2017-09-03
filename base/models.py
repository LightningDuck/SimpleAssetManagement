from django.db import models

# Create your models here.



class LocationDescription(models.Model):

    description_text = models.TextField()

    def __str__(self):
        return "{}".format(self.description_text)

class Location (models.Model):

    description = models.ForeignKey(LocationDescription)
    gps_coordinates_latitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    gps_coordinates_longitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)

    street_address_1 = models.CharField(max_length = 20, blank=True, null=True)
    street_address_2 = models.CharField(max_length = 20, blank=True, null=True)
    city = models.CharField(max_length = 20, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    state_region = models.CharField(max_length = 20, blank=True, null=True)
    country_code = models.CharField (max_length=2, blank=True, null=True)

    def __str__(self):
        return "{} {}".format("Location at ", self.description)

class AssetDescription(models.Model):


    description_text = models.TextField()

    def __str__(self):
        return "{}".format(self.description_text)

class Asset (models.Model):

    description = models.ForeignKey(AssetDescription, null=True)
    location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return "{}".format(self.description)





