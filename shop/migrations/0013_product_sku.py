# Generated by Django 4.2.3 on 2023-07-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_product_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
