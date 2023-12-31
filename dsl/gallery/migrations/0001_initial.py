# Generated by Django 4.2.6 on 2023-10-30 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
    ]
