from django.contrib import admin

# Register your models here.
from autohub.models import Manufacturer, CarType, Car

admin.site.register(Manufacturer)
admin.site.register(CarType)
admin.site.register(Car)