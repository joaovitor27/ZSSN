from django.urls import path

app_name = 'survivors'

from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view(), name='items'),
    path('survivors/', views.SurvivorListCreateAPIView.as_view(), name='survivors'),
    path('inventories/', views.InventoryListCreateAPIView.as_view(), name='inventories'),
]