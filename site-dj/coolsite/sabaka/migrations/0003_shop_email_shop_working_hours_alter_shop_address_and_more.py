# Generated by Django 5.2 on 2025-04-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabaka', '0002_delivery_promotion_shop_supplier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='shop',
            name='working_hours',
            field=models.CharField(max_length=100, null=True, verbose_name='Часы работы'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
