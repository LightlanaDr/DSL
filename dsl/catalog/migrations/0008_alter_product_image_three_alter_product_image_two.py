# Generated by Django 4.2.6 on 2023-11-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_image_three_product_image_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_three',
            field=models.ImageField(default='/images/products/1_JAfRO3x.jpg', upload_to='products/', verbose_name='Фото2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_two',
            field=models.ImageField(default='/images/products/1_JAfRO3x.jpg', upload_to='products/', verbose_name='Фото2'),
        ),
    ]