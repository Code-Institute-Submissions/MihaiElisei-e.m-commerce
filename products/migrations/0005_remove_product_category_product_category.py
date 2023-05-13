# Generated by Django 4.2.1 on 2023-05-13 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
