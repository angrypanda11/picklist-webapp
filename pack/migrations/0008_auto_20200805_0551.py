# Generated by Django 3.0.8 on 2020-08-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0007_auto_20200805_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='picked',
            field=models.CharField(default='未捡', max_length=10),
        ),
    ]
