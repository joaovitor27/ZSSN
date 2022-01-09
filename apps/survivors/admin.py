from django.contrib import admin

# Register your models here.
from .models import Survivor, Item, Inventory

admin.site.register(Survivor)
admin.site.register(Item)
admin.site.register(Inventory)
