# Generated by Django 2.1.7 on 2019-06-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_auto_20190606_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.FloatField(default=200.0, verbose_name='Prix'),
        ),
    ]