# Generated by Django 3.1 on 2020-09-16 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0016_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='batch_id',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='sku',
            field=models.CharField(max_length=150),
        ),
    ]
