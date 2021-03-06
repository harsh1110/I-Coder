# Generated by Django 3.1.7 on 2021-06-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/shop_img')),
                ('catagory', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
