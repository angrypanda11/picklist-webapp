from django.contrib import admin


# Register your models here.

from .models import Order


@admin.register(Order)
class OrderResource(admin.ModelAdmin):
    list_display = ('order_number', 'batch_id', 'sku', 'quantity', 'picked', 'notes')
