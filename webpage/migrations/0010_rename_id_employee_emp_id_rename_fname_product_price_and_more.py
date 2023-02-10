# Generated by Django 4.1.3 on 2022-11-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_employee_remove_product_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='id',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='fname',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='prod_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lname',
            new_name='prod_name',
        ),
        migrations.AddField(
            model_name='product',
            name='prod_onhand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]