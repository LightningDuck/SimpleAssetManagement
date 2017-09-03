from personnel.models import Person
from rest_framework import serializers


class PersonSerializer (serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'last_name', 'first_name', 'date_of_birth')
