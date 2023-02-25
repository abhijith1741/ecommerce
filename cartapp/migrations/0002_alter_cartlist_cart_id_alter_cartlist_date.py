# Generated by Django 4.1.4 on 2022-12-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cartlist',
            name='date',
            field=models.DateTimeField(auto_now=True, unique=True),
        ),
    ]