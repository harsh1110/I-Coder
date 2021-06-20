# Generated by Django 3.1.7 on 2021-06-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='static/blog_img')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
