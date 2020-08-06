from django.db import models


# Create your models here.
class Order(models.Model):
    batch_id = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    picked = models.CharField(max_length=5, default='')
    notes = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.batch_id
