# Generated by Django 5.1.3 on 2024-12-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0002_rename_address1_shippingaddress_shipping_address1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingaddress",
            name="shipping_address2",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
