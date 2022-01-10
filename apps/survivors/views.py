from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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


@api_view(['POST'])
def transaction_between_survivors(request):
   
    try:
        survivor1 = Survivor.objects.get(id=request.data.get('survivor1'), infected=False)
        survivor2 = Survivor.objects.get(id=request.data.get('survivor2'), infected=False)
        item_survivor1 = Item.objects.get(id=request.data.get('item_survivor1'))
        item_survivor2 = Item.objects.get(id=request.data.get('item_survivor2'))
        inventory_survivor1 = Inventory.objects.get(survivor=survivor1, item=item_survivor1)
        inventory_survivor2 = Inventory.objects.get(survivor=survivor2, item=item_survivor2)
    except Survivor.DoesNotExist:
        return Response({'message': _('Um dos sobreviventes não foi encontrado na base de dados ou está infectado.')})
    except Item.DoesNotExist:
        return Response({'message': _('Item não cadastrado no sistema.')})
    except Inventory.DoesNotExist:
        return Response({'message': _('Um dos sobreviventes não tem o item no seu inventário.')})
    item_survivor1_quantity = request.data.get('item_survivor1_quantity')
    item_survivor2_quantity = request.data.get('item_survivor2_quantity')
    if survivor1 != survivor2:
        points_quantity_survivor1 = item_survivor1.points * item_survivor1_quantity
        points_quantity_survivor2 = item_survivor2.points * item_survivor2_quantity
        if points_quantity_survivor1 == points_quantity_survivor2:
            inventory_survivor1.quantity -= item_survivor1_quantity
            inventory_survivor2.quantity -= item_survivor2_quantity
            add_item_survivor1 = Inventory.objects.get(survivor=survivor1, item=item_survivor2)
            add_item_survivor1.quantity += item_survivor2_quantity
            add_item_survivor1.save()
            add_item_survivor2 = Inventory.objects.get(survivor=survivor2, item=item_survivor1)
            add_item_survivor2.quantity += item_survivor2_quantity
            add_item_survivor2.save()
            if inventory_survivor1.quantity < 0:
                inventory_survivor1.quantity = 0
                inventory_survivor1.save()
            else:
                inventory_survivor1.save()
            if inventory_survivor2.quantity < 0:
                inventory_survivor2.quantity = 0
                inventory_survivor2.save()
            else:
                inventory_survivor2.save()
            return Response({'message': _('Transação realizada com sucesso.')})
        return Response({'message': _('Erro na transação. Verifique os dados fornecidos.')})
    return Response({'message': _("Sobrevivente não pode trocar item consigo mesmo.")})


@api_view(['POST'])
def mark_survivor_as_infected(request):
    """
    Marca um sobrevivente como infectado. É necessário fornecer a informação de 3 sobreviventes que confirmam a infecção e a informação do
    infectado.
    """
    try:
        survivor1 = Survivor.objects.get(id=request.data.get('survivor1'), infected=False)
        survivor2 = Survivor.objects.get(id=request.data.get('survivor2'), infected=False)
        survivor3 = Survivor.objects.get(id=request.data.get('survivor3'), infected=False)
        survivor_infected = Survivor.objects.get(id=request.data.get('survivor_infected'))
    except Survivor.DoesNotExist:
        return Response({'message': _('Confirme se todos os sobreviventes estão cadastrados no sistema e que não estão infectados.')})
    survivor_list = set([survivor1, survivor2, survivor3])
    if len(survivor_list) >= 3 and survivor_infected not in survivor_list:
        if survivor_infected.infected:
            return Response({'message': _('Sobrevivente já marcado como infectado.')})
        else:
            survivor_infected.infected = True
            survivor_infected.save()
        return Response({'message': _('Sobrevivente marcado como infectado.')})
    return Response({'message': _('Operação não realizada. É preciso três sobreviventes únicos e o suspeito de estar infectado não pode ser quem acusa.')})
