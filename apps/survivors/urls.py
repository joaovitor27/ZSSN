from django.urls import path

app_name = 'survivors'

from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view(), name='items'),
    path('survivors/', views.SurvivorListCreateAPIView.as_view(), name='survivors'),
    path('inventories/', views.InventoryListCreateAPIView.as_view(), name='inventories'),
    path('survivor-location-update/<int:survivor_id>/', views.SurvivorLocationUpdate.as_view(), name='survivor_location_update'),
    path('transactions/', views.transaction_between_survivors, name='transactions'),
    path('mark-survivor-infected/', views.mark_survivor_as_infected, name='mark_survivor_as_infected'),
    
]