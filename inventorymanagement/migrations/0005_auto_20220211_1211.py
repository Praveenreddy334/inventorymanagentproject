# Generated by Django 3.0.7 on 2022-02-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorymanagement', '0004_auto_20220211_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory_transaction',
            name='goods_receipt_note',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory_transaction',
            name='quantity_ordered',
            field=models.PositiveIntegerField(),
        ),
    ]
