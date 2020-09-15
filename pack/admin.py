from django.contrib import admin


# Register your models here.

from .models import Order, Export


@admin.register(Order)
class OrderResource(admin.ModelAdmin):
    list_display = ('order_number', 'batch_id', 'sku', 'quantity', 'picked', 'notes')


@admin.register(Export)
class Dictionary(admin.ModelAdmin):
    list_display = ('product_code', 'price', 'discount', 'quantity')


# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 1
#
#
# @admin.register(Entry)
# class Entry(admin.ModelAdmin):
#     inlines = [ProductInline]
#     list_display = ['sku']
