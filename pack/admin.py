from django.contrib import admin


# Register your models here.

from .models import Order, Dictionary, Entry, Product


@admin.register(Order)
class OrderResource(admin.ModelAdmin):
    list_display = ('order_number', 'batch_id', 'sku', 'quantity', 'picked', 'notes')


@admin.register(Dictionary)
class Dictionary(admin.ModelAdmin):
    list_display = ('sku', 'product_code', 'multiplier', 'price')


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Entry)
class Entry(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['sku']
