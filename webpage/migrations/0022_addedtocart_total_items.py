# Generated by Django 4.1.5 on 2023-01-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0021_delete_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedtocart',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]
