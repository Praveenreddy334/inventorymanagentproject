# Generated by Django 3.0.7 on 2022-02-09 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('transaction_id', models.IntegerField()),
                ('goods_receipt_note', models.CharField(blank=True, max_length=20, null=True)),
                ('goods_return_note', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity_ordered', models.IntegerField()),
                ('quantity_delivered', models.IntegerField()),
                ('quantity_before', models.IntegerField()),
                ('quantity_after', models.IntegerField()),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventary', to='inventorymanagement.Inventory_Items')),
            ],
        ),
    ]