from django.db import models
from base.models import Asset

from datetime import date

# Create your models here.

class Person(Asset):

    id_number = models.CharField(max_length = 10)
    last_name = models.CharField(max_length= 30, default="")
    first_name = models.CharField(max_length=20, default ="")
    date_of_birth = models.DateField(default = date.today)
