# Generated by Django 4.2.2 on 2023-06-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_vendorapply_vendorrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorapply',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]