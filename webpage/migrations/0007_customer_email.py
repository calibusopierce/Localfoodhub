# Generated by Django 4.1.3 on 2022-11-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_alter_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]