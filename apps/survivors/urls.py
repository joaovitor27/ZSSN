from django.urls import path

app_name = 'survivors'

from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view(), name='items'),
]