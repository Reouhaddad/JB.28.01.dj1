# Generated by Django 5.0.1 on 2024-02-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/IMG_0151-new.jpg', null=True, upload_to=''),
        ),
    ]
