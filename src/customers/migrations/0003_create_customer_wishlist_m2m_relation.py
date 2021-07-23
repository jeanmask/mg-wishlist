# Generated by Django 3.2.5 on 2021-07-23 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_create_product_model"),
        ("customers", "0002_create_wishlist_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="wishlist",
            field=models.ManyToManyField(
                related_name="_customers_customer_wishlist_+",
                through="customers.Wishlist",
                to="products.Product",
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="+", to="customers.customer"
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="+", to="products.product"
            ),
        ),
    ]
