# Generated by Django 4.1.3 on 2022-11-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_remove_orderdetail_brgy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
