# Generated by Django 4.1.3 on 2022-11-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('full_address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.RemoveField(
            model_name='product',
            name='full_address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone_number',
        ),
    ]
