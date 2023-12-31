# Generated by Django 4.2.2 on 2023-06-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customerprofile_cover_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vendor_request')),
                ('nid_picture', models.ImageField(upload_to='vendor_nid_picture')),
                ('frist_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=255)),
                ('registere_number', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('shop_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
