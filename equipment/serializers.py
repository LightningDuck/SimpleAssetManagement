from rest_framework import serializers
from equipment.models import Equipment


class EquipmentSerializer(serliizers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id', 'serial_number')