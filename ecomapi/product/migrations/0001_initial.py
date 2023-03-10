# Generated by Django 4.0.1 on 2022-11-12 12:54

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField(max_length=10)),
                ('category', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to=product.models.file_directory_path)),
                ('spec1', models.CharField(max_length=50)),
                ('spec2', models.CharField(max_length=50)),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('line3', models.CharField(max_length=50)),
                ('line4', models.CharField(max_length=50)),
            ],
        ),
    ]
