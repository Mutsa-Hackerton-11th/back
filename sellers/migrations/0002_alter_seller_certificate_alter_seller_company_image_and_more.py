# Generated by Django 4.2.4 on 2023-08-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='seller',
            name='company_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='seller',
            name='company_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='company_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='copy_bankbook',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
