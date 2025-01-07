# Generated by Django 5.1.3 on 2025-01-07 14:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100, unique=True)),
                ('change_type', models.CharField(choices=[('Stock Increase', 'Stock Increase'), ('Stock Decrease', 'Stock Decrease'), ('No Change', 'No Change')], default='No Change', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('low_stock', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('change_reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_changes', to='inventory.changereason')),
            ],
        ),
    ]
