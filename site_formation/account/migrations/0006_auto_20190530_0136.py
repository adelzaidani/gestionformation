# Generated by Django 2.1.7 on 2019-05-29 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190530_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_profile',
            field=models.ImageField(blank=True, upload_to='account'),
        ),
    ]
