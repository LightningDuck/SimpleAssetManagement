from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from personnel.models import Person
from personnel.serializers import PersonSerializer

@csrf_exempt
def person_list(request):

    if request.method == "GET":
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data=JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def person_detail (request, pk):

    try:
        person = Person.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status="400")
    elif request.method == "DELETE":
        person.delete()
        return HttpResponse(status="204")

