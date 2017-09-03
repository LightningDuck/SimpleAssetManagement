from rest_framework import serializers
from base.models import Location, LocationDescription, Asset, AssetDescription


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('street_address_1', 'street_address_2',
                  'city', 'county', 'state_region', 'country',
                  'gps_coordinates_latitude', 'gps_coordinates_longitude')

class LocationDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('description_text')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ()

class AssetDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDescription
        fields = ('description_text')
