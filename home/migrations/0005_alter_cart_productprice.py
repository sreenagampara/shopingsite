# Generated by Django 4.0.1 on 2022-03-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='productprice',
            field=models.FloatField(),
        ),
    ]
