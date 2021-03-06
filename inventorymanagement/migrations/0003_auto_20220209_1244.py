# Generated by Django 3.0.7 on 2022-02-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorymanagement', '0002_auto_20220209_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory_items',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory_transaction',
            name='quantity_after',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory_transaction',
            name='quantity_before',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory_transaction',
            name='quantity_delivered',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory_transaction',
            name='quantity_ordered',
            field=models.PositiveIntegerField(),
        ),
    ]
