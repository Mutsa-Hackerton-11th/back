# Generated by Django 4.2.4 on 2023-08-15 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_sold_alter_product_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='products.product'),
        ),
    ]
