from django.db import models


# Create your models here.
class Order(models.Model):
    batch_id = models.CharField(max_length=150)
    order_number = models.CharField(max_length=150)
    sku = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    picked = models.CharField(max_length=5, default='')
    notes = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.order_number


class Export(models.Model):
    product_code = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=1, max_digits=3, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_code


class Item(models.Model):
    item_sku = models.CharField(max_length=60)


class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50)
    multiplier = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)


# class Entry(models.Model):
#     sku = models.CharField(max_length=60)
#
#     def __str__(self):
#         return self.sku
#
#
# class Product(models.Model):
#     entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     product_code = models.CharField(max_length=50)
#     multiplier = models.IntegerField(default=0)
#     price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
#
#     def __str__(self):
#         return self.product_code
