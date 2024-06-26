# Generated by Django 4.2.4 on 2023-08-08 12:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('company_level', models.IntegerField(default=1)),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('certificate', models.ImageField(null=True, upload_to='')),
                ('copy_bankbook', models.ImageField(null=True, upload_to='')),
                ('company_url', models.URLField(null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('company_image', models.ImageField(null=True, upload_to='')),
                ('company_info', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
