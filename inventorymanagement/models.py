from django.db import models

# Create your models here.

class Inventory_Items(models.Model):
    distributor_id=models.CharField(max_length=30)
    product_id=models.CharField(max_length=30)
    product_name=models.CharField(max_length=30)
    quantity=models.PositiveIntegerField()
    # is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name

class Inventory_Transaction(models.Model):
    distributor_id =models.CharField(max_length=30)
    product_id = models.CharField(max_length=30)
    inventory_id=models.ForeignKey(Inventory_Items,on_delete=models.CASCADE,related_name='inventary')
    transaction_id=models.CharField(max_length=100)
    goods_receipt_note=models.PositiveIntegerField(null=True,blank=True)
    goods_return_note = models.PositiveIntegerField(null=True,blank=True)
    quantity_ordered=models.PositiveIntegerField()
    damaged_items=models.PositiveIntegerField(null=True,blank=True)
    quantity_delivered=models.PositiveIntegerField()
    quantity_before=models.PositiveIntegerField()
    quantity_after=models.PositiveIntegerField()

