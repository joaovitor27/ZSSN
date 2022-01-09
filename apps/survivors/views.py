from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Item, Survivor, Inventory
from .serializers import ItemSerializer, SurvivorSerializer, InventorySerializer
from apps.survivors import serializers
# Create your views here.


class ItemListCreateAPIView(ListCreateAPIView):
    
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAdminUser]


class SurvivorListCreateAPIView(ListCreateAPIView):

    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all()

