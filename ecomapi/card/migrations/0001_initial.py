# Generated by Django 4.0.1 on 2022-11-12 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel')),
            ],
        ),
    ]
