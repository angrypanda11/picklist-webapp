# Generated by Django 3.0.8 on 2020-08-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0005_auto_20200805_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='picked',
            field=models.CharField(default='', max_length=10),
        ),
    ]