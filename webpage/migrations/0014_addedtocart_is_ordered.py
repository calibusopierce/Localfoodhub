# Generated by Django 4.1.4 on 2022-12-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0013_addedtocart_orders_productlist_delete_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedtocart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]
