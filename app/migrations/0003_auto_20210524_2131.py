# Generated by Django 3.0.7 on 2021-05-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210524_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_pr_price',
            field=models.CharField(max_length=30),
        ),
    ]