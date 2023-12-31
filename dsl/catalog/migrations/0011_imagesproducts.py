# Generated by Django 4.2.6 on 2023-11-27 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_product_image_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.product')),
            ],
        ),
    ]
