from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Item, Survivor, Inventory
from .serializers import ItemSerializer, SurvivorSerializer, InventorySerializer

# Create your views here.


class ItemListCreateAPIView(ListCreateAPIView):
    
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAdminUser]


class SurvivorListCreateAPIView(ListCreateAPIView):

    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all()


class InventoryListCreateAPIView(ListCreateAPIView):

    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    permissions_classes = [IsAdminUser]


class SurvivorLocationUpdate(APIView):

    def patch(self, request, survivor_id):
        survivor = get_object_or_404(Survivor, pk=survivor_id)
        serializer = SurvivorSerializer(survivor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': _('Atualização não realizada.')})

