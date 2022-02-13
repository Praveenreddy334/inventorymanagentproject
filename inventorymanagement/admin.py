from django.contrib import admin
from .models import Inventory_Items,Inventory_Transaction
# Register your models here.
admin.site.register(Inventory_Items),
admin.site.register(Inventory_Transaction),