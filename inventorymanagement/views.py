from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Inventory_Items,Inventory_Transaction

from .serializers import Inventory_Items_Serializer,Inventory_Transactions_Serializer

# Create your views here.

class RemoveInventory(APIView):
     def post(self,request):
        Product_id=request.data['product_id']
        Product_name=request.data['product_name']
        Quantity=request.data['quantity']#from salesman
        object=Inventory_Items.objects.get(product_id=Product_id)
        print(object)
        count = 100
        if object.quantity>=Quantity:
            count+= 1
            initial_quantity=object.quantity
            left_quantity=object.quantity-Quantity
            object.quantity=left_quantity#updating quantity in Inventory_Items
            object.save()
            #u inventory_transaction
            distributor_id=object.distributor_id
            product_id=Product_id
            inventory_id=object
            transaction_id=count
            goods_receipt_note=Quantity
            goods_return_note=0
            quantity_ordered=Quantity
            quantity_delivered=Quantity
            quantity_before=initial_quantity
            quantity_after=left_quantity
            inventory_update=Inventory_Transaction(distributor_id=distributor_id,product_id=product_id,inventory_id=object,transaction_id=transaction_id,goods_receipt_note=goods_receipt_note,goods_return_note=goods_return_note,quantity_ordered=quantity_ordered,quantity_delivered=quantity_delivered,quantity_before=quantity_before,quantity_after=quantity_after)
            inventory_update.save()
            inventory_transaction_id=Inventory_Transaction.objects.last().id
            transaction=Inventory_Transaction.objects.get(id=inventory_transaction_id)
            serializer=Inventory_Transactions_Serializer(transaction)
            return Response(serializer.data)
        elif object.quantity < Quantity and object.quantity>0:
            initial_quantity = object.quantity
            left_quantity=0
            object.quantity=0
            object.save()
            distributor_id = object.distributor_id
            product_id = Product_id
            inventory_id = object
            transaction_id = count
            goods_receipt_note = initial_quantity
            goods_return_note =0
            quantity_ordered = Quantity
            quantity_delivered =initial_quantity
            quantity_before = initial_quantity
            quantity_after=0
            inventory_update = Inventory_Transaction(distributor_id=distributor_id,product_id=product_id,inventory_id=object, transaction_id=transaction_id,goods_receipt_note=goods_receipt_note,goods_return_note=goods_return_note,quantity_ordered=quantity_ordered,quantity_delivered=quantity_delivered,quantity_before=quantity_before, quantity_after=quantity_after)
            inventory_update.save()
            inventory_transaction_id=Inventory_Transaction.objects.last().id
            transaction = Inventory_Transaction.objects.get(id=inventory_transaction_id)
            serializer = Inventory_Transactions_Serializer(transaction)
            return Response(serializer.data)
        else:
            if object.quantity==0:
                return Response("there is no stock available of this product")


class AddInventory(APIView):
    def post(self,request,type):
        if type=='company':
            Distributor_id=request.data['distributor_id']
            Product_id=request.data['product_id']
            Product_name = request.data['product_name']
            Quantity = request.data['quantity']
            try:
                # if product id exist....
                object = Inventory_Items.objects.get(product_id=Product_id)
                initial_quantity = object.quantity
                final_quantity = initial_quantity + Quantity
                object.quantity = final_quantity
                object.save()
                # transaction=Inventory_Items.objects.get(product_id=Product_id)
                serializer=Inventory_Items_Serializer(object)
                return Response(serializer.data)
            except:
                inventory_update = Inventory_Items(distributor_id=Distributor_id, product_id=Product_id,product_name=Product_name, quantity=Quantity)
                inventory_update.save()
                transaction = Inventory_Items.objects.get(product_id=Product_id)
                serializer = Inventory_Items_Serializer(transaction)
                return Response(serializer.data)
        if type=='return':
            Product_id = request.data['product_id']
            Product_name = request.data['product_name']
            Quantity = request.data['quantity']  # from salesman
            Goods_Receipt=request.data['goods_receipt_note']
            Goods_Return=request.data['goods_return_note']
            Damaged_Items=request.data['damaged_items']
            object=Inventory_Items.objects.get(product_id=Product_id)
            print(object)
            try:
                object.quantity >= Quantity
                initial_quantity = object.quantity
                left_quantity = object.quantity - Quantity
                object.quantity = Goods_Return-Damaged_Items+left_quantity  # updating quantity in Inventory_Items
                object.save()
                inventory_update = Inventory_Transaction(distributor_id=object.distributor_id, product_id=Product_id,inventory_id=object, transaction_id=102,goods_receipt_note=Goods_Receipt,goods_return_note=Goods_Return, quantity_ordered= Quantity,quantity_delivered=Quantity, quantity_before=initial_quantity,quantity_after=object.quantity)
                inventory_update.save()
                inventory_transaction_id = Inventory_Transaction.objects.last().id
                transaction = Inventory_Transaction.objects.get(id=inventory_transaction_id)
                serializer = Inventory_Transactions_Serializer(transaction)
                return Response(serializer.data)
            except:
                return Response("no sufficient stock available")











