from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.viewsets import ModelViewSet

class MenuItemsView(generics.ListCreateAPIView) :
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView) :
    serializer_class = MenuSerializer 
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet) :
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer  