# Generated by Django 4.1.13 on 2024-01-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_stripe_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(blank=True, default=0, max_length=220, null=True),
        ),
    ]
