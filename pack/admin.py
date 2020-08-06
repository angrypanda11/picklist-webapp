from django.contrib import admin


# Register your models here.

from .models import Order


@admin.register(Order)
class OrderResource(admin.ModelAdmin):
    list_display = ('batch_id', 'order_number', 'sku', 'quantity', 'picked', 'notes')
