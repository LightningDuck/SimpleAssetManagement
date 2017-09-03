from django.shortcuts import render

from utils.decorators import ajax, template
from .models import Location
from .serializers import LocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import pdb

@template("../templates/index.html")
def index(request):

    return dict()

@template("../templates/list_locations.html")
def list_locations(request):

    locations = Location.objects.all()

    return dict(locations=locations)

class LocationListVoew(APIView):
    pass

