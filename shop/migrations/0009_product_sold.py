# Generated by Django 4.2.3 on 2023-07-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_prodcut_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]