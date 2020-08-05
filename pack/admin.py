from django.contrib import admin


# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Order


@admin.register(Order)
class OrderResource(ImportExportModelAdmin):
    list_display = ('batch_id', 'order_number', 'sku', 'quantity', 'picked', 'notes')
