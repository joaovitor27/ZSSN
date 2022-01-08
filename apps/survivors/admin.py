from django.contrib import admin

# Register your models here.
from .models import StockItems, Sobreviventes, accusations, inventory

admin.site.register(StockItems)
admin.site.register(Sobreviventes)
admin.site.register(accusations)
admin.site.register(inventory)