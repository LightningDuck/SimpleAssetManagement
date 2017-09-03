from django.contrib import admin

# Register your models here.

from .models import Location, LocationDescription


admin.site.register(Location)
admin.site.register(LocationDescription)
