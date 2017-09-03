from django.db import models
from base.models import Asset

# Create your models here.

class Equipment(Asset):

    serial_number = models.CharField(max_length=20)

    def __init__(self):
        pass
