from django.shortcuts import render

from utils.decorators import ajax, template
from .models import Location
from .serializers import LocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

import pdb

@template("../templates/index.html")
def index(request):

    return dict()


class LocationListView(ListView):

    template_name = "../templates/list_locations.html"
    model = Location

    # def get(self.request):
    #     return HttpResponse()

    def get_context_data(self, **kwargs):

        context = super(LocationListView, self).get_context_data(**kwargs)
        context["locations"] = Location.objects.all()

        return context


@template("../templates/list_locations.html")
def list_locations(request):

    locations = Location.objects.all()

    return dict(locations=locations)


class APILocationListView(APIView):
     pass

