# Generated by Django 3.1.7 on 2021-06-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210613_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
