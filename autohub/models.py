from django.db import models

# Create your models here.
from django.utils import timezone

FUEL_CHOICES = [('diesel', 'DIESEL'), ('unleaded95', 'UNLEADED95')]

TRANSMISSION_CHOICES = [('manual', 'MANUAL'), ('automatic', 'AUTOMATIC')]

YEAR_CHOICES = [('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')]


class Manufacturer(models.Model):
    brand = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    description = models.TextField()
    established = models.DateField()
    cover = models.URLField(max_length=200, null=True)
    cover2 = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ['id']


class CarType(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField()
    established = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Car(models.Model):
    title = models.CharField(max_length=50)

    brand = models.ForeignKey(Manufacturer, null=True, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=50, null=True)

    car_type = models.ForeignKey(CarType, null=True, on_delete=models.CASCADE)
    car_type_name = models.CharField(max_length=50, null=True)

    fuel = models.CharField(choices=FUEL_CHOICES, null=True, max_length=100)
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, null=True, max_length=100)
    year = models.CharField(choices=YEAR_CHOICES, null=True, max_length=100)

    country = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=15, null=True)
    description = models.TextField()

    cover = models.URLField(max_length=200, null=True)
    cover1 = models.URLField(max_length=200, null=True)
    video = models.URLField(max_length=200, null=True)

    owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
