from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.response import Response

from autohub.models import Car, Manufacturer, CarType
from autohub.permissions import IsOwnerOrReadOnly
from autohub.serializers import CarSerializer, ManufacturerSerializer, CarTypeSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


def home_page(request):
    return render(request, 'home_page.html')


class CarList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('title', 'brand', 'car_type')

    # Return the jsonArray with the "Cars" name inside a JSON object

    # def list(self, request, *args, **kwargs):
    #     self.object_list = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(self.object_list, many=True)
    #
    #     return Response({'Cars': serializer.data})


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ManufacturerList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('brand', 'country')


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class TypeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
