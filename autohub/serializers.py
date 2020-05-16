from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

from autohub.models import Car, Manufacturer, FUEL_CHOICES, TRANSMISSION_CHOICES, YEAR_CHOICES, CarType


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'title', 'brand', 'brand_name', 'car_type', 'car_type_name', 'fuel',
                  'transmission', 'year', 'country', 'price', 'description',
                  'cover', 'cover1', 'video', 'owner']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'brand', 'country', 'description', 'established', 'cover', 'cover2']


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name', 'description', 'established']


class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'cars']
