# Generated by Django 3.1 on 2020-08-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0009_auto_20200806_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('product_code', models.CharField(max_length=50)),
                ('true_quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
