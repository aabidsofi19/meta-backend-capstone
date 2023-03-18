from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer
from .models import Menu,Booking

class MenuItemsView(generics.ListCreateAPIView) :
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView) :
    serializer_class = MenuSerializer 
    queryset = Menu.objects.all()