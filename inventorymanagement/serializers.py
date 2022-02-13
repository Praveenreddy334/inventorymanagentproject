from rest_framework import serializers
from .models import Inventory_Items,Inventory_Transaction

class Inventory_Items_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory_Items
        fields='__all__'

class Inventory_Transactions_Serializer(serializers.ModelSerializer):
    inventory_id=Inventory_Items_Serializer(read_only=True)
    class Meta:
        model=Inventory_Transaction
        fields=('distributor_id','product_id','transaction_id','goods_receipt_note','goods_return_note','quantity_ordered','quantity_delivered','quantity_before','quantity_after','inventory_id')

