# Generated by Django 2.2.4 on 2019-08-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0009_product_to_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_to_order',
            name='is_ordered',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product_to_order',
            name='toppings',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_to_order',
            name='total_toppings',
            field=models.FloatField(null=True),
        ),
    ]